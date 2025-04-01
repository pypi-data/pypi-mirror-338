import numpy as np
import sys
import traceback
from contextlib import contextmanager

comm = None
size = 1
rank = 0
name = ""
mpi = False
main = True


def activate_mpi(collective_mpi=True, terminate_on_close=True):
    global comm, size, rank, name, main, mpi, TERMINATE_ON_CLOSE, COLLECTIVE_MPI
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    size = MPI.COMM_WORLD.Get_size()
    rank = MPI.COMM_WORLD.Get_rank()
    name = MPI.Get_processor_name()
    mpi = True
    main = rank == 0
    COLLECTIVE_MPI = collective_mpi
    TERMINATE_ON_CLOSE = terminate_on_close


MPIClassInterfaceAttributes = {
    'close',
    'release_mpi_workers',
    'use_rank',
    'cls',
    'work_loop',
    'object',
    '__class__',
    'get_input',
    'do_task',
    'run_task',
    'closed'}


TERMINATE_ON_CLOSE = True  # MPI workers (rank>0) will terminate (sys.exit) when the close command is called via rank0
COLLECTIVE_MPI = True  # rank0 acts as a single point of contact (scatters command+arg and gathers results)


def main_run(f, *args, **kwargs):
    if main:
        r = f(*args, **kwargs)
        if COLLECTIVE_MPI:
            return r[0]
    else:
        try:
            f(*args, **kwargs)
        except BaseException:
            pass
        r = None
    return comm.bcast(r)


class MPIClassInterface():
    def __init__(self, cls, args_lst):
        self.closed = False
        if len(args_lst) > size:
            if rank == 0:
                raise Exception(f"Not enough mpi slots. Slots: {size}, Requested: {len(args_lst)}")
            return
        self.cls = cls
        if rank < len(args_lst):
            self.object = cls(*args_lst[rank])
        else:
            class Dummy():
                def close(self):
                    pass

                def __getattr__(self, name):
                    raise AttributeError(
                        f"Rank {rank} trying to access {name}, but only {len(args_lst)} instances of {cls.__name__} exists")
            self.object = Dummy()

        self.use_rank = np.array([True] * size)
        self.use_rank[len(args_lst):] = False
        if rank > 0 and COLLECTIVE_MPI:
            self.work_loop()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def work_loop(self):
        while True:
            method, args, kwargs = comm.scatter(None)
            comm.gather(self.do_task(method, args, kwargs))
            if method == 'exit_work_loop':
                break
            if method == 'close':
                if TERMINATE_ON_CLOSE:
                    # comm.gather(f'Exit, rank {rank}')
                    print("sys.exit", rank, flush=True)
                    self.closed = True
                    sys.exit(0)
                else:
                    raise ChildProcessError('MPI worker done')

    def do_task(self, method, args, kwargs):
        try:
            if method == 'skip' or method == 'exit_work_loop':
                res = None
            elif method == 'setattr':
                name, value = args
                res = setattr(self.object, name, value)
            else:
                res = getattr(self.object, method)
                if hasattr(res, '__call__'):
                    res = res(*args, **kwargs)
        except BaseException as e:
            res = (e, traceback.format_exc())
        return res

    def run_task(self, input_lst):
        assert rank == 0, "other ranks should be in work_loop when invoking run_task. For non-collective mpi, do_task should be used"
        comm.scatter(input_lst, root=0)
        method, args, kwargs = input_lst[0]
        res = self.do_task(method, args, kwargs)

        use_rank = self.use_rank

        res = [res for i, res in enumerate(comm.gather(res, root=0)) if use_rank[i]]
        for r in res:
            if isinstance(r, tuple) and len(r) > 1 and isinstance(r[0], BaseException):
                raise r[0].__class__(r[1])
        return res

    def get_input(self, name, i, args, kwargs):
        use_rank = self.use_rank
        N = np.sum(use_rank)
        j = sum(use_rank[:i])  # needed for subsets

        # if COLLECTIVE_MPI:
        #    j = sum(use_rank[:i])
        # else:
        #    j = 0

        if use_rank[i]:
            def get_arg(arg):
                if isinstance(arg, list) and len(arg) == N:
                    return arg[j]
                else:
                    return arg

            return (name, [get_arg(arg) for arg in args], {k: get_arg(v) for k, v in kwargs.items()})
        else:
            return ('skip', [], {})

    def __getattribute__(self, name):
        if name in MPIClassInterfaceAttributes:
            return object.__getattribute__(self, name)
        elif not COLLECTIVE_MPI and not self.use_rank[rank]:
            raise ChildProcessError(f'MPI worker {rank} not used')

        def wrap(*args, **kwargs):
            if COLLECTIVE_MPI:
                inp = [self.get_input(name, i, args, kwargs) for i in range(size)]
                return self.run_task(inp)
            else:
                method, args, kwargs = self.get_input(name, rank, args, kwargs)
                return [self.do_task(method, args, kwargs)]
        try:
            att = getattr(self.object, name)
        except AttributeError as e:
            raise type(e)(f'Rank {rank}: {e}').with_traceback(sys.exc_info()[2])

        if hasattr(att, '__call__'):
            res = wrap
        else:
            res = wrap()
        return res

    def __setattr__(self, name, value):
        if (COLLECTIVE_MPI and rank > 0) or name in MPIClassInterfaceAttributes:
            return object.__setattr__(self, name, value)
        else:
            inp = [self.get_input('setattr', i, (name, value), {}) for i in range(size)]
            if COLLECTIVE_MPI:
                return self.run_task(inp)
            else:
                return self.do_task(*inp[rank])

    def __getitem__(self, slice):
        use_rank = np.full_like(self.use_rank, False)
        use_rank[np.where(self.use_rank)[0][slice]] = True
        if np.all(self.use_rank == use_rank):
            return self
        return SubsetMPIClassInterface(self.cls, self.object, use_rank)

    @contextmanager
    def release_mpi_workers(self):
        global COLLECTIVE_MPI
        """Use to release mpi_workers. All object statements including 'release_mpi_workers' must be protected by 'if mpi_interface.main:' """
        if COLLECTIVE_MPI:
            if rank == 0:
                self.run_task([('exit_work_loop', [], {}) for _ in range(size)])
            COLLECTIVE_MPI = False
            try:
                yield self
            finally:
                COLLECTIVE_MPI = True
                if rank > 0 and not self.closed:
                    self.work_loop()

    def close(self):

        if not self.closed:

            if COLLECTIVE_MPI:
                if rank == 0:
                    res = self.run_task([('close', [], {}) for _ in range(size)])
            else:
                res = self.do_task('close', [], {})
            self.closed = True


class SubsetMPIClassInterface(MPIClassInterface):
    def __init__(self, cls, object, use_rank):
        self.use_rank = use_rank
        self.cls = cls
        self.object = object

    def __getitem__(self, slice):
        l = np.arange(np.sum(self.use_rank))
        if np.all(l == l[slice]):
            return self
        raise Exception('Cannot make subset of SubsetMPIClassInterface')

    def close(self):
        raise Exception('Cannot close SubsetMPIClassInterface. Please close all instances at once')

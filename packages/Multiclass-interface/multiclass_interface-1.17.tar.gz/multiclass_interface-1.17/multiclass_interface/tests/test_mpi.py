import os
import sys
import time
import traceback
from numpy import testing as npt
import pytest

from multiclass_interface.mpi_interface import MPIClassInterface
from multiclass_interface.multiprocess_interface import ProcessClass
import numpy as np
from multiclass_interface.tests.my_test_cls import MyTest
from multiclass_interface import mpi_interface


def mpirun(f):
    if 'main()' in traceback.format_stack()[0]:
        n = f.__name__

        def wrap():
            exe = sys.executable.replace("\\", "/")
            cmd = f'''mpirun -n 4 {exe} -c "from multiclass_interface.tests.test_mpi import {n}; {n}()"'''
            # print(cmd)
            assert os.system(cmd) == 0, n
        wrap.__name__ = n
        return wrap
    else:
        return f


@mpirun
def test_mpi_collective_too_few_slots():
    mpi_interface.activate_mpi()
    N = 4
    rank = mpi_interface.rank

    try:
        with MPIClassInterface(MyTest, [(i + 1,) for i in range(N + 1)]) as m:
            pass
        assert rank in [1, 2, 3]
    except Exception as e:
        assert rank == 0
        assert str(e) == 'Not enough mpi slots. Slots: 4, Requested: 5'


@mpirun
def test_mpi_collective_MyTest():
    mpi_interface.activate_mpi()
    N = 4
    rank = mpi_interface.rank

    with MPIClassInterface(MyTest, [(i + 1,) for i in range(N)]) as m:
        if mpi_interface.main:
            i = m.get_id()
            npt.assert_array_equal(i, np.arange(N) + 1)

        with m.release_mpi_workers():
            assert m.get_id() == [rank + 1]

        assert m.get_id() == [1, 2, 3, 4]
        i = mpi_interface.main_run(lambda: m.get_id())
        npt.assert_array_equal(i, 1)

        assert m[1].get_id() == [2]

        try:
            npt.assert_array_equal(m[1:3].get_id(), np.arange(1, 3) + 1)
        except ChildProcessError:
            pass

        m.x = "hello"
        assert m.x == ['hello'] * 4

        assert m.return_input([101, 102, 103, 104])[0] == f'1 got: ({101},) and ' + '{}'
        m.x = 'hello'
        assert m.x == ['hello'] * 4
        m[1::2].x = 'world'
        assert m[:].x == ['hello', 'world', 'hello', 'world']

        m.release_mpi_workers()
        m.x = [1, 2, 3, 4]
        assert m.x == [1, 2, 3, 4]
        m.y = list(np.array(m.x) + 10)
        assert m.y == [11, 12, 13, 14]
        t = time.time()
        m.work(1)
        t = time.time() - t
        assert t < 1.1

        with pytest.raises(Exception, match='Cannot close SubsetMPIClassInterface. Please close all instances at once'):
            m[:3].close()
        with pytest.raises(Exception, match='Cannot make subset of SubsetMPIClassInterface'):
            m[:3][1]


@mpirun
def test_mpi_collective_close_released_mpi_workers():
    mpi_interface.activate_mpi()
    N = 4
    rank = mpi_interface.rank
    with MPIClassInterface(MyTest, [(i + 1,) for i in range(N)]) as m:
        with m.release_mpi_workers():
            m.close()


@mpirun
def test_mpi_ProcessClass():
    mpi_interface.activate_mpi()
    with ProcessClass(MyTest) as cls:
        myTest = cls(1)
        assert myTest.get_id() == 1


@mpirun
def test_non_collective_mpi2():
    mpi_interface.activate_mpi(collective_mpi=False)
    rank = mpi_interface.rank
    N = 3
    with MPIClassInterface(MyTest, [(i + 10,) for i in range(N)]) as m:

        try:
            assert m.get_id()[0] == rank + 10, m.get_id()
            main_id = mpi_interface.main_run(lambda: m.get_id())
            assert main_id == [10], (rank, main_id)
            assert rank < N  # rank > N will fail with ChildProcessError
            assert m.return_input([101, 102, 103])[0] == f'{rank + 10} got: ({rank + 101},) and ' + '{}'
            m.x = 'hello'
            assert m.x[0] == 'hello', m.x[0]
            m.x = [1, 2, 3]
            assert m.x[0] == rank + 1
            m.y = m.x[0] + 10
            assert m.y[0] == rank + 11
        except ChildProcessError:
            pass

        if rank == 3:
            with pytest.raises(AttributeError, match='Rank 3 trying to access cls, but only 3 instances of MyTest exists'):
                m.object.cls


@mpirun
def test_mpi_non_collective_MyTest():
    mpi_interface.activate_mpi(collective_mpi=False)
    rank = mpi_interface.rank
    N = 4

    with MPIClassInterface(MyTest, [(i + 1,) for i in range(N)]) as m:
        i = m.get_id()[0]
        assert i == rank + 1
        i = mpi_interface.main_run(lambda: m.get_id())
        npt.assert_array_equal(i, 1)  # id of rank0 broadcast to all
        try:
            assert m[1:3].get_id()[0] == rank + 1
        except ChildProcessError:
            assert rank in [0, 3]

        # rank>0 fails, but only rank=0 is needed, so should not fail
        mpi_interface.main_run(lambda rank=rank: 1 / [0, 1][rank == 0])

        assert m.return_input([101, 102, 103, 104])[0] == f'{rank + 1} got: ({rank + 101},) and ' + '{}'
        m.x = "hello"
        assert m.x[0] == 'hello'

        m[1::2].x = 'world'
        assert m.x[0] == ['hello', 'world'][rank % 2]

        try:
            assert m[1::2].x[0] == 'world'
            assert m[1::2][:].x[0] == 'world'
        except ChildProcessError:
            pass

        m.x = [1, 2, 3, 4]
        assert m.x[0] == rank + 1

        m.y = m.x[0] + 10
        assert m.y[0] == rank + 11
        t = time.time()
        m.work(1)
        t = time.time() - t
        assert t < 1.1

        with pytest.raises(Exception, match='Cannot close SubsetMPIClassInterface. Please close all instances at once'):
            m[:3].close()
        with pytest.raises(Exception, match='Cannot make subset of SubsetMPIClassInterface'):
            m[:3][1]


@mpirun
def test_multiprocessinterface_tests():
    from multiclass_interface.tests.test_multiprocessinterface import test_attribute, test_missing_attribute, test_execption, test_setattr, test_setattr_method
    mpi_interface.activate_mpi()

    try:
        with MPIClassInterface(MyTest, [(1,), (2,), (3,)]) as mpici:
            for f in [test_attribute, test_missing_attribute, test_execption, test_setattr, test_setattr_method]:
                f(mpici)
    except ChildProcessError:
        pass


@mpirun
def test_multiprocessinterface_tests_diff_interface():
    from multiclass_interface.tests.test_multiprocessinterface import test_attribute, test_missing_attribute, test_execption, test_setattr, test_setattr_method
    mpi_interface.activate_mpi(terminate_on_close=False)

    for f in [test_attribute, test_missing_attribute, test_execption, test_setattr, test_setattr_method]:
        # print (mpi_interface.rank, f.__name__,flush=True)
        try:
            with MPIClassInterface(MyTest, [(1,), (2,), (3,)]) as mpici:
                f(mpici)
        except ChildProcessError:
            pass
    sys.exit(0)

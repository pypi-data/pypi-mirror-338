import numpy as np
import pytest
import os
from mpi4py import MPI
from mumps4py.mumps_solver import MumpsSolver

@pytest.mark.skipif("cmumps" not in os.getenv("MUMPS_SOLVERS", "").split(","), reason="cmumps not selected")
def test_solve_single():
    solver = MumpsSolver(verbose=False, system="complex64")

    dtype = np.complex64
    
    n = 5
    irn = np.array([0,1,3,4,1,0,4,2,1,2,0,2], dtype=np.int32)
    jcn = np.array([1,2,2,4,0,0,1,3,4,1,2,2], dtype=np.int32)
    a = np.array([3.0,-3.0,2.0,1.0,3.0,2.0,4.0,2.0,6.0,-1.0,4.0,1.0], dtype=dtype)
    b = np.array([20.0,24.0,9.0,6.0,13.0], dtype=dtype)

    solver.set_rcd_centralized(irn+1, jcn+1, a, n)
    solver._mumps_call(job=1)

    rhs = b.copy()
    solver._mumps_call(job=2)
    solver.set_rhs_centralized(rhs)
    solver._mumps_call(3)

    if MPI.COMM_WORLD.Get_rank()==0:
        assert np.allclose(rhs, [np.complex64(1), np.complex64(2), np.complex64(3),
                                 np.complex64(4), np.complex64(5)], atol=1e-10)

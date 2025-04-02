__all__ = ['DMUMPS_STRUC_C', 'dmumps_c.h']

from libc cimport stdint

cdef extern from 'dmumps_c.h':  

    ctypedef int MUMPS_INT
    ctypedef double DMUMPS_COMPLEX
    ctypedef double DMUMPS_REAL
    ctypedef stdint.int64_t MUMPS_INT8

    char* MUMPS_VERSION

    ctypedef struct c_DMUMPS_STRUC_C 'DMUMPS_STRUC_C':

        MUMPS_INT sym
        MUMPS_INT par
        MUMPS_INT job
        MUMPS_INT comm_fortran
        MUMPS_INT icntl[60]
        MUMPS_INT keep[500]
        DMUMPS_REAL cntl[15]
        DMUMPS_REAL dkeep[230]
        MUMPS_INT8 keep8[150]
        MUMPS_INT n
        MUMPS_INT nblk
        MUMPS_INT nz_alloc
        MUMPS_INT nz
        MUMPS_INT8 nnz
        MUMPS_INT* irn
        MUMPS_INT* jcn
        DMUMPS_COMPLEX* a
        MUMPS_INT nz_loc
        MUMPS_INT8 nnz_loc
        MUMPS_INT* irn_loc
        MUMPS_INT* jcn_loc
        DMUMPS_COMPLEX* a_loc
        MUMPS_INT nelt
        MUMPS_INT* eltptr
        MUMPS_INT* eltvar
        DMUMPS_COMPLEX* a_elt
        MUMPS_INT* blkptr
        MUMPS_INT* blkvar
        MUMPS_INT* perm_in
        MUMPS_INT* sym_perm
        MUMPS_INT* uns_perm
        DMUMPS_REAL* colsca
        DMUMPS_REAL* rowsca
        MUMPS_INT colsca_from_mumps
        MUMPS_INT rowsca_from_mumps
        DMUMPS_COMPLEX* rhs
        DMUMPS_COMPLEX* redrhs
        DMUMPS_COMPLEX* rhs_sparse
        DMUMPS_COMPLEX* sol_loc
        DMUMPS_COMPLEX* rhs_loc
        MUMPS_INT* irhs_sparse
        MUMPS_INT* irhs_ptr
        MUMPS_INT* isol_loc
        MUMPS_INT* irhs_loc
        MUMPS_INT nrhs
        MUMPS_INT lrhs
        MUMPS_INT lredrhs
        MUMPS_INT nz_rhs
        MUMPS_INT lsol_loc
        MUMPS_INT nloc_rhs
        MUMPS_INT lrhs_loc
        MUMPS_INT schur_mloc
        MUMPS_INT schur_nloc
        MUMPS_INT schur_lld
        MUMPS_INT mblock
        MUMPS_INT nblock
        MUMPS_INT nprow
        MUMPS_INT npcol
        MUMPS_INT info[80]
        MUMPS_INT infog[80]
        DMUMPS_REAL rinfo[40]
        DMUMPS_REAL rinfog[40]
        MUMPS_INT deficiency
        MUMPS_INT* pivnul_list
        MUMPS_INT* mapping
        MUMPS_INT size_schur
        MUMPS_INT* listvar_schur
        DMUMPS_COMPLEX* schur
        MUMPS_INT instance_number
        DMUMPS_COMPLEX* wk_user
        char ooc_tmpdir[256]
        char ooc_prefix[64]
        char write_problem[256]
        MUMPS_INT lwk_user
        char save_dir[256]
        char save_prefix[256]
        MUMPS_INT metis_options[40]

    void c_dmumps_c 'dmumps_c' (c_DMUMPS_STRUC_C *) nogil

cdef extern from "stddef.h":
    size_t sizeof()

def get_mumps_int_size():
    """Return the size of MUMPS_INT in bytes."""
    return sizeof(MUMPS_INT)

cdef class DMUMPS_STRUC_C:
    cdef c_DMUMPS_STRUC_C obj

    property sym:
        def __get__(self): return self.obj.sym
        def __set__(self, value): self.obj.sym = value

    property par:
        def __get__(self): return self.obj.par
        def __set__(self, value): self.obj.par = value

    property job:
        def __get__(self): return self.obj.job
        def __set__(self, value): self.obj.job = value

    property comm_fortran:
        def __get__(self): return self.obj.comm_fortran
        def __set__(self, value): self.obj.comm_fortran = value

    property icntl:
        def __get__(self):
            cdef MUMPS_INT[:] view = self.obj.icntl
            return view 

    property keep:
        def __get__(self):
            cdef MUMPS_INT[:] view = self.obj.keep
            return view 

    property cntl:
        def __get__(self):
            cdef DMUMPS_REAL[:] view = self.obj.cntl
            return view 

    property dkeep:
        def __get__(self):
            cdef DMUMPS_REAL[:] view = self.obj.dkeep
            return view 

    property keep8:
        def __get__(self):
            cdef MUMPS_INT8[:] view = self.obj.keep8
            return view 

    property n:
        def __get__(self): return self.obj.n
        def __set__(self, value): self.obj.n = value

    property nblk:
        def __get__(self): return self.obj.nblk
        def __set__(self, value): self.obj.nblk = value

    property nz_alloc:
        def __get__(self): return self.obj.nz_alloc
        def __set__(self, value): self.obj.nz_alloc = value

    property nz:
        def __get__(self): return self.obj.nz
        def __set__(self, value): self.obj.nz = value

    property nnz:
        def __get__(self): return self.obj.nnz
        def __set__(self, value): self.obj.nnz = value

    property irn:
        def __get__(self): return <long> self.obj.irn
        def __set__(self, long value): self.obj.irn = <MUMPS_INT*> value

    property jcn:
        def __get__(self): return <long> self.obj.jcn
        def __set__(self, long value): self.obj.jcn = <MUMPS_INT*> value

    property a:
        def __get__(self): return <long> self.obj.a
        def __set__(self, long value): self.obj.a = <DMUMPS_COMPLEX*> value

    property nz_loc:
        def __get__(self): return self.obj.nz_loc
        def __set__(self, value): self.obj.nz_loc = value

    property nnz_loc:
        def __get__(self): return self.obj.nnz_loc
        def __set__(self, value): self.obj.nnz_loc = value

    property irn_loc:
        def __get__(self): return <long> self.obj.irn_loc
        def __set__(self, long value): self.obj.irn_loc = <MUMPS_INT*> value

    property jcn_loc:
        def __get__(self): return <long> self.obj.jcn_loc
        def __set__(self, long value): self.obj.jcn_loc = <MUMPS_INT*> value

    property a_loc:
        def __get__(self): return <long> self.obj.a_loc
        def __set__(self, long value): self.obj.a_loc = <DMUMPS_COMPLEX*> value

    property nelt:
        def __get__(self): return self.obj.nelt
        def __set__(self, value): self.obj.nelt = value

    property eltptr:
        def __get__(self): return <long> self.obj.eltptr
        def __set__(self, long value): self.obj.eltptr = <MUMPS_INT*> value

    property eltvar:
        def __get__(self): return <long> self.obj.eltvar
        def __set__(self, long value): self.obj.eltvar = <MUMPS_INT*> value

    property a_elt:
        def __get__(self): return <long> self.obj.a_elt
        def __set__(self, long value): self.obj.a_elt = <DMUMPS_COMPLEX*> value

    property blkptr:
        def __get__(self): return <long> self.obj.blkptr
        def __set__(self, long value): self.obj.blkptr = <MUMPS_INT*> value

    property blkvar:
        def __get__(self): return <long> self.obj.blkvar
        def __set__(self, long value): self.obj.blkvar = <MUMPS_INT*> value

    property perm_in:
        def __get__(self): return <long> self.obj.perm_in
        def __set__(self, long value): self.obj.perm_in = <MUMPS_INT*> value

    property sym_perm:
        def __get__(self): return <long> self.obj.sym_perm
        def __set__(self, long value): self.obj.sym_perm = <MUMPS_INT*> value

    property uns_perm:
        def __get__(self): return <long> self.obj.uns_perm
        def __set__(self, long value): self.obj.uns_perm = <MUMPS_INT*> value

    property colsca:
        def __get__(self): return <long> self.obj.colsca
        def __set__(self, long value): self.obj.colsca = <DMUMPS_REAL*> value

    property rowsca:
        def __get__(self): return <long> self.obj.rowsca
        def __set__(self, long value): self.obj.rowsca = <DMUMPS_REAL*> value

    property colsca_from_mumps:
        def __get__(self): return self.obj.colsca_from_mumps
        def __set__(self, value): self.obj.colsca_from_mumps = value

    property rowsca_from_mumps:
        def __get__(self): return self.obj.rowsca_from_mumps
        def __set__(self, value): self.obj.rowsca_from_mumps = value

    property rhs:
        def __get__(self): return <long> self.obj.rhs
        def __set__(self, long value): self.obj.rhs = <DMUMPS_COMPLEX*> value

    property redrhs:
        def __get__(self): return <long> self.obj.redrhs
        def __set__(self, long value): self.obj.redrhs = <DMUMPS_COMPLEX*> value

    property rhs_sparse:
        def __get__(self): return <long> self.obj.rhs_sparse
        def __set__(self, long value): self.obj.rhs_sparse = <DMUMPS_COMPLEX*> value

    property sol_loc:
        def __get__(self): return <long> self.obj.sol_loc
        def __set__(self, long value): self.obj.sol_loc = <DMUMPS_COMPLEX*> value

    property rhs_loc:
        def __get__(self): return <long> self.obj.rhs_loc
        def __set__(self, long value): self.obj.rhs_loc = <DMUMPS_COMPLEX*> value

    property irhs_sparse:
        def __get__(self): return <long> self.obj.irhs_sparse
        def __set__(self, long value): self.obj.irhs_sparse = <MUMPS_INT*> value

    property irhs_ptr:
        def __get__(self): return <long> self.obj.irhs_ptr
        def __set__(self, long value): self.obj.irhs_ptr = <MUMPS_INT*> value

    property isol_loc:
        def __get__(self): return <long> self.obj.isol_loc
        def __set__(self, long value): self.obj.isol_loc = <MUMPS_INT*> value

    property irhs_loc:
        def __get__(self): return <long> self.obj.irhs_loc
        def __set__(self, long value): self.obj.irhs_loc = <MUMPS_INT*> value

    property nrhs:
        def __get__(self): return self.obj.nrhs
        def __set__(self, value): self.obj.nrhs = value

    property lrhs:
        def __get__(self): return self.obj.lrhs
        def __set__(self, value): self.obj.lrhs = value

    property lredrhs:
        def __get__(self): return self.obj.lredrhs
        def __set__(self, value): self.obj.lredrhs = value

    property nz_rhs:
        def __get__(self): return self.obj.nz_rhs
        def __set__(self, value): self.obj.nz_rhs = value

    property lsol_loc:
        def __get__(self): return self.obj.lsol_loc
        def __set__(self, value): self.obj.lsol_loc = value

    property nloc_rhs:
        def __get__(self): return self.obj.nloc_rhs
        def __set__(self, value): self.obj.nloc_rhs = value

    property lrhs_loc:
        def __get__(self): return self.obj.lrhs_loc
        def __set__(self, value): self.obj.lrhs_loc = value

    property schur_mloc:
        def __get__(self): return self.obj.schur_mloc
        def __set__(self, value): self.obj.schur_mloc = value

    property schur_nloc:
        def __get__(self): return self.obj.schur_nloc
        def __set__(self, value): self.obj.schur_nloc = value

    property schur_lld:
        def __get__(self): return self.obj.schur_lld
        def __set__(self, value): self.obj.schur_lld = value

    property mblock:
        def __get__(self): return self.obj.mblock
        def __set__(self, value): self.obj.mblock = value

    property nblock:
        def __get__(self): return self.obj.nblock
        def __set__(self, value): self.obj.nblock = value

    property nprow:
        def __get__(self): return self.obj.nprow
        def __set__(self, value): self.obj.nprow = value

    property npcol:
        def __get__(self): return self.obj.npcol
        def __set__(self, value): self.obj.npcol = value

    property info:
        def __get__(self):
            cdef MUMPS_INT[:] view = self.obj.info
            return view 

    property infog:
        def __get__(self):
            cdef MUMPS_INT[:] view = self.obj.infog
            return view 

    property rinfo:
        def __get__(self):
            cdef DMUMPS_REAL[:] view = self.obj.rinfo
            return view 

    property rinfog:
        def __get__(self):
            cdef DMUMPS_REAL[:] view = self.obj.rinfog
            return view 

    property deficiency:
        def __get__(self): return self.obj.deficiency
        def __set__(self, value): self.obj.deficiency = value

    property pivnul_list:
        def __get__(self): return <long> self.obj.pivnul_list
        def __set__(self, long value): self.obj.pivnul_list = <MUMPS_INT*> value

    property mapping:
        def __get__(self): return <long> self.obj.mapping
        def __set__(self, long value): self.obj.mapping = <MUMPS_INT*> value

    property size_schur:
        def __get__(self): return self.obj.size_schur
        def __set__(self, value): self.obj.size_schur = value

    property listvar_schur:
        def __get__(self): return <long> self.obj.listvar_schur
        def __set__(self, long value): self.obj.listvar_schur = <MUMPS_INT*> value

    property schur:
        def __get__(self): return <long> self.obj.schur
        def __set__(self, long value): self.obj.schur = <DMUMPS_COMPLEX*> value

    property instance_number:
        def __get__(self): return self.obj.instance_number
        def __set__(self, value): self.obj.instance_number = value

    property wk_user:
        def __get__(self): return <long> self.obj.wk_user
        def __set__(self, long value): self.obj.wk_user = <DMUMPS_COMPLEX*> value

    property ooc_tmpdir:
        def __get__(self):
            cdef char[:] view = self.obj.ooc_tmpdir
            return view 

    property ooc_prefix:
        def __get__(self):
            cdef char[:] view = self.obj.ooc_prefix
            return view 

    property write_problem:
        def __get__(self):
            cdef char[:] view = self.obj.write_problem
            return view 

    property lwk_user:
        def __get__(self): return self.obj.lwk_user
        def __set__(self, value): self.obj.lwk_user = value

    property save_dir:
        def __get__(self):
            cdef char[:] view = self.obj.save_dir
            return view 

    property save_prefix:
        def __get__(self):
            cdef char[:] view = self.obj.save_prefix
            return view 

    property metis_options:
        def __get__(self):
            cdef MUMPS_INT[:] view = self.obj.metis_options
            return view 

def dmumps_c(DMUMPS_STRUC_C s not None):
    with nogil:
        c_dmumps_c(&s.obj)

__version__ = (<bytes> MUMPS_VERSION).decode('ascii')



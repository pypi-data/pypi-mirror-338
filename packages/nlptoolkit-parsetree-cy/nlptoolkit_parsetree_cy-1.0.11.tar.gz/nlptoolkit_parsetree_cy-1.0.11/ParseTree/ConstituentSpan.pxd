from ParseTree.Symbol cimport Symbol


cdef class ConstituentSpan:

    cdef Symbol __constituent
    cdef int __start
    cdef int __end

    cpdef int getStart(self)
    cpdef int getEnd(self)
    cpdef Symbol getConstituent(self)

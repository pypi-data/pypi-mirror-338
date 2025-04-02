from ParseTree.ParseTree cimport ParseTree


cdef class TreeBank:

    cdef list parse_trees

    cpdef int size(self)
    cpdef int wordCount(self, bint excludeStopWords)
    cpdef ParseTree get(self, int index)
    cpdef removeTree(self, int i)

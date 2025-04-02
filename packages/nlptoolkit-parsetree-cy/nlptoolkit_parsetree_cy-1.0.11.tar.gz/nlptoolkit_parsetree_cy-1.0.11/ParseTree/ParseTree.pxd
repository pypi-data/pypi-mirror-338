from ParseTree.ParseNode cimport ParseNode


cdef class ParseTree:

    cdef ParseNode root
    cdef str name

    cpdef ParseNode nextLeafNode(self, ParseNode parseNode)
    cpdef ParseNode previousLeafNode(self, ParseNode parseNode)
    cpdef int nodeCountWithMultipleChildren(self)
    cpdef int nodeCount(self)
    cpdef int leafCount(self)
    cpdef setName(self, str name)
    cpdef str getName(self)
    cpdef bint isFullSentence(self)
    cpdef save(self, str fileName)
    cpdef correctParents(self)
    cpdef removeXNodes(self)
    cpdef ParseNode getRoot(self)
    cpdef int wordCount(self, bint excludeStopWords)
    cpdef list constituentSpanList(self)

    cpdef constructor1(self, ParseNode root)

    cpdef constructor2(self, str fileName)

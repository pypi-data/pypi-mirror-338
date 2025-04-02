from ParseTree.NodeCondition.NodeCondition cimport NodeCondition
from ParseTree.ParseNode cimport ParseNode


cdef class NodeCollector:

    cdef NodeCondition __condition
    cdef ParseNode __root_node

    cpdef __collectNodes(self, ParseNode parseNode, list collected)
    cpdef list collect(self)

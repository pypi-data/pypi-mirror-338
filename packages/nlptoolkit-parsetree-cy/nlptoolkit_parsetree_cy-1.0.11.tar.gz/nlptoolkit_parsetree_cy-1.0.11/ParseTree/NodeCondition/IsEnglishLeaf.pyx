from ParseTree.NodeCondition.IsLeaf cimport IsLeaf
from ParseTree.ParseNode cimport ParseNode


cdef class IsEnglishLeaf(IsLeaf):

    cpdef bint satisfies(self, ParseNode parseNode):
        """
        Implemented node condition for English leaf node.

        PARAMETERS
        ----------
        parseNode : ParseNode
            Checked node.

        RETURNS
        -------
        bool
            If the node is a leaf node and is not a dummy node, returns true; false otherwise.
        """
        cdef str data, parent_data
        if parseNode.numberOfChildren() == 0:
            data = parseNode.getData().getName()
            parent_data = parseNode.getParent().getData().getName()
            if "*" in data or (data == "0" and parent_data == "-NONE-"):
                return False
            return True
        return False

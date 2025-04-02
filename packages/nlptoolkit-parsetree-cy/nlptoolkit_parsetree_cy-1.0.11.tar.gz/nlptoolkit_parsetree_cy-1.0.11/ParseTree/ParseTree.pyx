import os

from ParseTree.NodeCollector cimport NodeCollector
from ParseTree.NodeCondition.IsEnglishLeaf cimport IsEnglishLeaf


cdef class ParseTree:

    sentence_labels = ["SINV", "SBARQ", "SBAR", "SQ", "S"]

    cpdef constructor1(self, ParseNode root):
        """
        Basic constructor for a ParseTree. Initializes the root node with the input.
        :param root: Root node of the tree
        """
        self.root = root

    cpdef constructor2(self, str fileName):
        """
        Another constructor of the ParseTree. The method takes the file containing a single line as input and constructs
        the whole tree by calling the ParseNode constructor recursively.
        :param fileName: File containing a single line for a ParseTree
        """
        cdef str line
        self.name = os.path.split(fileName)[1]
        input_file = open(fileName, "r", encoding="utf8")
        line = input_file.readline()
        if "(" in line and ")" in line:
            line = line[line.index("(") + 1:line.rindex(")")].strip()
            self.root = ParseNode(None, line, False)
        else:
            self.root = None
        input_file.close()

    def __init__(self, rootOrFileName=None):
        """
        Basic constructor for a ParseTree. Initializes the root node with the input.

        PARAMETERS
        ----------
        rootOrFileName : ParseNode
            Root node of the tree
        """
        if isinstance(rootOrFileName, ParseNode):
            self.constructor1(rootOrFileName)
        elif isinstance(rootOrFileName, str):
            self.constructor2(rootOrFileName)

    cpdef ParseNode nextLeafNode(self, ParseNode parseNode):
        """
        Gets the next leaf node after the given leaf node in the ParseTree.

        PARAMETERS
        ----------
        parseNode : ParseNode
            ParseNode for which next node is calculated.

        RETURNS
        -------
        ParseNode
            Next leaf node after the given leaf node.
        """
        cdef NodeCollector node_collector
        cdef list leaf_list
        cdef int i
        node_collector = NodeCollector(self.root, IsEnglishLeaf())
        leaf_list = node_collector.collect()
        for i in range(len(leaf_list) - 1):
            if leaf_list[i] == parseNode:
                return leaf_list[i + 1]
        return None

    cpdef setName(self, str name):
        """
        Mutator for the name attribute.
        :param name: Name of the parse tree.
        """
        self.name = name

    cpdef str getName(self):
        """
        Accessor for the name attribute.
        :return: Name of the parse tree.
        """
        return self.name

    cpdef ParseNode previousLeafNode(self, ParseNode parseNode):
        """
        Gets the previous leaf node before the given leaf node in the ParseTree.

        PARAMETERS
        ----------
        parseNode : ParseNode
            ParseNode for which previous node is calculated.

        RETURNS
        -------
        ParseNode
            Previous leaf node before the given leaf node.
        """
        cdef NodeCollector node_collector
        cdef list leaf_list
        cdef int i
        node_collector = NodeCollector(self.root, IsEnglishLeaf())
        leaf_list = node_collector.collect()
        for i in range(1, len(leaf_list)):
            if leaf_list[i] == parseNode:
                return leaf_list[i - 1]
        return None

    cpdef int nodeCountWithMultipleChildren(self):
        """
        Calls recursive method to calculate the number of all nodes, which have more than one children.

        RETURNS
        -------
        int
            Number of all nodes, which have more than one children.
        """
        return self.root.nodeCountWithMultipleChildren()

    cpdef int nodeCount(self):
        """
        Calls recursive method to calculate the number of all nodes tree.

        RETURNS
        -------
        int
            Number of all nodes in the tree.
        """
        return self.root.nodeCount()

    cpdef int leafCount(self):
        """
        Calls recursive method to calculate the number of all leaf nodes in the tree.

        RETURNS
        -------
        int
            Number of all leaf nodes in the tree.
        """
        return self.root.leafCount()

    cpdef bint isFullSentence(self):
        """
        Checks if the sentence is a full sentence or not. A sentence is a full sentence is its root tag is S, SINV, etc.
        :return: True if the sentence is a full sentence, false otherwise.
        """
        if self.root is not None and self.root.data.getName() in self.sentence_labels:
            return True
        return False

    cpdef save(self, str fileName):
        """
        Saves the tree into the file with the given file name. The output file only contains one line representing tree.

        PARAMETERS
        ----------
        fileName : str
            Output file name
        """
        output_file = open(fileName, "w", encoding="utf8")
        output_file.write("( " + self.__str__() + " )\n")
        output_file.close()

    cpdef correctParents(self):
        """
        Calls recursive method to restore the parents of all nodes in the tree.
        """
        self.root.correctParents()

    cpdef removeXNodes(self):
        """
        Calls recursive method to remove all nodes starting with the symbol X. If the node is removed, its children are
        connected to the next sibling of the deleted node.
        """
        self.root.removeXNodes()

    cpdef ParseNode getRoot(self):
        """
        Accessor method for the root node.

        RETURNS
        -------
        ParseNode
            Root node
        """
        return self.root

    def __str__(self) -> str:
        """
        Calls recursive function to convert the tree to a string.

        RETURNS
        -------
        str
            A string which contains all words in the tree.
        """
        return self.root.__str__()

    cpdef int wordCount(self, bint excludeStopWords):
        """
        Calls recursive function to count the number of words in the tree.

        PARAMETERS
        ----------
        excludeStopWords : bool
            If true, stop words are not counted.

        RETURNS
        -------
        int
            Number of words in the tree.
        """
        return self.root.wordCount(excludeStopWords)

    cpdef list constituentSpanList(self):
        """
        Generates a list of constituents in the parse tree and their spans.

        RETURNS
        -------
        list
            A list of constituents in the parse tree and their spans.
        """
        cdef list result
        result = []
        self.root.constituentSpanList(1, result)
        return result

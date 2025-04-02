cdef class ConstituentSpan:

    def __init__(self, constituent: Symbol, start: int, end: int):
        """
        Constructor for the ConstituentSpan class. ConstituentSpan is a structure for storing constituents or phrases in
        a sentence with a specific label. Sets the attributes.
        :param constituent: Label of the span.
        :param start: Start index of the span.
        :param end: End index of the span.
        """
        self.__constituent = constituent
        self.__start = start
        self.__end = end

    cpdef int getStart(self):
        """
        Accessor for the start attribute
        :return: Current start
        """
        return self.__start

    cpdef int getEnd(self):
        """
        Accessor for the end attribute
        :return: Current end
        """
        return self.__end

    cpdef Symbol getConstituent(self):
        """
        Accessor for the constituent attribute
        :return: Current constituent
        """
        return self.__constituent
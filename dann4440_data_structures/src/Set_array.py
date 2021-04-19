"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-12"
-------------------------------------------------------
"""
from copy import deepcopy
class Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Set.
        Use: s = Set()
        -------------------------------------------------------
        Returns:
            Initializes an empty set.
        -------------------------------------------------------
        """

        self._values = []

        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the set is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the set is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the set.
        Use: n = len(s)
        -------------------------------------------------------
        Returns:
            the number of values in the set.
        -------------------------------------------------------
        """
        return len(self._values)

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the set.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of key in the set, -1 if key is not found (int)
        -------------------------------------------------------
        """
        found = False
        i = 0
        while not found and i<len(self._values):
            if self._values[i]==key:
                found = True
            else:
                i+=1
        if not found:
            i=-1

        return i

    def insert(self, i, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the set.
        Use: b = s.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            inserted - True if the value was inserted at i, False otherwise.
                value is inserted at position i or appended to the end of the set
                if i > len(s) only if value is unique in the set (boolean)
        -------------------------------------------------------
        """
        inserted = False
        already_in = self._linear_search(value)
        if already_in==-1:
            if i<len(self._values):
                one = self._values[:i]
                two = self._values[i:]
                self._values = one+[value]+two
            else:
                self._values.append(value)
            inserted = True

        return inserted

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the set that matches key.
        Use: value = s.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        value = None
        in_set = self._linear_search(key)
        if in_set>0:
            value = self._values.pop(in_set)

        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in the set that matches key.
        Use: value = s.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find in an empty set"
        value = None
        found = self._linear_search(key)
        if found !=-1:
            value = key
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the set (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty set"

        value = deepcopy(self._values[0])

        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in the set.
        Use: n = s.index( key )
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the full value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """

        i = self._linear_search(key)

        return i


    def _valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(set) to len(set) - 1
        Use: assert self._valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = len(self._values)
        return -n <= i < n
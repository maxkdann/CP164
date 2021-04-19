"""
-------------------------------------------------------
Linked version of the Stack ADT.
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-24"
-------------------------------------------------------
"""
from copy import deepcopy
class _Stack_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a stack node that contains a copy of value
        and a link to the next node in the stack.
        Use: node = _Stack_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Stack node (_Stack_Node)
        Returns:
            a new _Stack_Node object (_Stack_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Values are stored in a 
        linked structure.
        Use: source = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._top = None

    def _move_top_to_top(self, source):
        """
        -------------------------------------------------------
        Moves the top node from the source stack to the target stack.
        The target stack contains the old top node of the source stack.
        The source stack top is updated. Equivalent of
        self.push(source.pop()), but moves nodes, not data.
        Use: target._move_top_to_top(source)
        -------------------------------------------------------
        Parameters:
            source - a linked stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._top is not None, "Cannot move the top of an empty stack"

        temp = source._top
        source._top = source._top._next
        temp._next = self._top
        self._top = temp
        return

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of source.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        new_top = None

        while self._top is not None:
            temp = self._top._next
            self._top._next = new_top
            new_top = self._top
            self._top = temp
        self._top = new_top
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked stack (Stack)
            source2 - an linked stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        while source1._top is not None and source2._top is not None:
            self._move_top_to_top(source1)
            self._move_top_to_top(source2)

        while source1._top is not None:
            self._move_top_to_top(source1)

        while source2._top is not None:
            self._move_top_to_top(source2)
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if source is empty, False otherwise
        -------------------------------------------------------
        """
        return self._top is None

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of source.
        Attempting to peek at an empty stack throws an exception.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of source (?)
        -------------------------------------------------------
        """
        assert self._top is not None, "Cannot peek at an empty stack"

        value = deepcopy(self._top._value)
        return value

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from source. Attempting to pop from an empty stack
        throws an exception.
        Use: value = source.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert self._top is not None, "Cannot pop from an empty stack"

        value = self._top._value
        self._top = self._top._next
        return value

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of source.
        Use: source.push(value)
        -------------------------------------------------------
        Parameters:
            value - value to be added to source (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._top = _Stack_Node(value, self._top)
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values 
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        target1 = Stack()
        target2 = Stack()
        left = True

        while self._top is not None:

            if left:
                target1._move_top_to_top(self)
            else:
                target2._move_top_to_top(self)
            left = not left
        return target1, target2

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from top to bottom.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            _value - the next value in source (?)
        -------------------------------------------------------
        """
        current = self._top

        while current is not None:
            yield current._value
            current = current._next


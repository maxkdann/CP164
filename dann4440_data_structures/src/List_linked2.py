"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 A
__updated__ = "2019-06-18"
-------------------------------------------------------
"""
# pylint: disable=W0212

from copy import deepcopy


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, self._front)

        if self._rear is None:
            # List is empty - update the rear of the List..
            self._rear = node
        # Update the front of the List.
        self._front = node
        self._count += 1
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Negative index adjustment.
        if i < 0:
            i = self._count + i

        if i <= 0:
            # Add value to the front of the list
            self.prepend(value)
        elif i >= self._count:
            # Add value to the end of the list
            self.append(value)
        else:
            # Add elsewhere in the list - not to front or rear
            j = 0
            previous = None
            current = self._front

            while j < i:
                # Find the proper location in the List
                previous = current
                current = current._next
                j += 1
            # Create the new node.
            node = _List_Node(value, current)
            previous._next = node
            self._count += 1
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0

        while current is not None and current._value != key:
            previous = current
            current = current._next
            index += 1

        if current is None:
            index = -1

        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # search list for key.
        previous, current, _ = self._linear_search(key)

        if current is None:
            # Key is not found.
            value = None
        else:
            value = current._value
            self._count -= 1

            if previous is None:
                # Remove the first node.
                self._front = self._front._next

                if self._front is None:
                    # List is empty, update _rear.
                    self._rear = None
            else:
                # Remove any other node.
                previous._next = current._next

                if previous._next is None:
                    # Last node was removed, update _rear.
                    self._rear = previous
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = self._front._value
        self._front = self._front._next
        self._count -= 1

        if self._front is None:
            # Last node has been removed
            self._rear = None
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        while self._front is not None and self._front._value == key:
            # The front node contains the value to be removed
            self._front = self._front._next
            self._count -= 1

        if self._front is None:
            # All nodes have been removed
            self._front = None
            self._rear = None
            self._count = 0
        else:
            previous = self._front
            current = self._front._next

            while current is not None:
                # Remove key from the rest of the list
                if current._value == key:
                    # Do not update previous
                    self._count -= 1
                    previous._next = current._next
                else:
                    previous = current
                current = current._next
            # Update the rear node
            self._rear = previous
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)

        if current is not None:
            value = deepcopy(current._value)
        else:
            value = None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        value = deepcopy(self._front._value)
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        _, _, i = self._linear_search(key)
        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        current = self._front

        if i < 0:
            # negative index - convert to positive
            i = self._count + i
        j = 0

        while j < i:
            current = current._next
            j += 1

        value = deepcopy(current._value)
        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        current = self._front

        if i < 0:
            # negative index - convert to positive
            i = self._count + i
        j = 0

        while j < i:
            current = current._next
            j += 1

        current._value = deepcopy(value)
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)
        return current is not None

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        max_node = self._front
        current = self._front._next

        while current is not None:
            if max_node._value < current._value:
                max_node = current
            current = current._next
        max_data = deepcopy(max_node._value)
        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        min_node = self._front
        current = self._front._next

        while current is not None:
            if min_node._value > current._value:
                min_node = current
            current = current._next
        min_data = deepcopy(min_node._value)
        return min_data

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        number = 0
        current = self._front

        while current is not None:
            if key == current._value:
                number += 1
            current = current._next
        return number

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self._rear = self._front
        previous = None
        current = self._front

        while current is not None:
            temp = current._next
            current._next = previous
            previous = current
            current = temp

        self._front = previous
        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains
        one and only one of each value formerly present in the list.
        The first occurrence of each value is preserved.
        Use: sl.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        key_node = self._front

        while key_node is not None:
            # Loop through every node - compare each node with the rest
            previous = key_node
            current = key_node._next

            while current is not None:
                # Always search to the end of the list (may have > 1 duplicate)
                if current._value == key_node._value:
                    # Remove the current node by connecting the node before it
                    # to the node after it.
                    self._count -= 1
                    previous._next = current._next
                else:
                    previous = current
                # Move to the _next node.
                current = current._next
            # Update the rear
            self._rear = previous
            # Check for duplicates of the _next remaining node in the list
            key_node = key_node._next
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches args.
        Use: value = lst.pop(args)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (?)
                args[0], if it exists, is the index
        Returns:
            value - if args exists, the value at position args, otherwise the last
                value in the list, value is removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        if pln is not prn:
            # Swap only if two nodes are not the same node

            if pln is None:
                # Make r the new front
                left = self._front
                self._front = prn._next
            else:
                left = pln._next
                pln._next = prn._next

            if prn is None:
                # Make l the new front
                right = self._front
                self._front = left
            else:
                right = prn._next
                prn._next = left

            # Swap next pointers
            # lst._next, r._next = r._next, lst._next
            temp = left._next
            left._next = right._next
            right._next = temp
            # Update the rear
            if right._next is None:
                self._rear = right
            elif left._next is None:
                self._rear = left
        return

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values as
                target in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != target._count:
            identical = False
        else:
            source_node = self._front
            target_node = target._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
        return identical

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        left = True

        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left

        return target1, target2

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    self.append(value)

            source1_node = source1_node._next
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in new list.
                self.append(value)
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in current list.
                self.append(value)

            source2_node = source2_node._next
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits source into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = source.split_th()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        # Initialize both temporary pointers to beginning of the list.
        hare = self._front
        tortoise = self._front

        while hare is not None and hare._next is not None:
            # Move hare down two nodes.
            hare = hare._next._next

            if hare is not None:
                # Update tortoise only if hare is not None.
                tortoise = tortoise._next

        # Split the list.
        if tortoise is not None:
            target1._front = self._front
            target1._rear = tortoise
            target2._front = tortoise._next
            tortoise._next = None
            target2._count = self._count // 2

            if target2._count > 0:
                target2._rear = self._rear
            target1._count = self._count - target2._count
            self._count = 0
            self._front = None
            self._rear = None
        return target1, target2

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        # Split
        middle = self._count // 2 + self._count % 2
        previous = None
        current = self._front

        for _ in range(middle):
            previous = current
            current = current._next

        # Define target1
        target1._front = self._front
        target1._rear = previous

        if previous is not None:
            previous._next = None

        # Define target2
        target1._count = middle
        target2._count = self._count - middle

        target2._front = current

        if target2._count > 0:
            target2._rear = self._rear

        # Clean up self
        self._front = None
        self._rear = None
        self._count = 0
        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values < key,
        and target2 contains all values >= key.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()

        while self._front is not None:

            if self._front._value < key:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
        return target1, target2

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values
        in targets is maintained.
        Use: target1, target2 = lst.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        # Split
        while self._front is not None:

            if func(self._front._value):
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
        return target1, target2

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: target = lst.copy()
        -------------------------------------------------------
        Returns:
            target - a copy of self (List)
        -------------------------------------------------------
        """
        target = List()

        if self._front is not None:
            # Set up the new list front.
            target._front = _List_Node(self._front._value, None)
            previous = target._front
            current = self._front._next

            while current is not None:
                # Add a node in the new list.
                new_node = _List_Node(current._value, None)
                previous._next = new_node
                previous = new_node
                # Move to the next node in the current list.
                current = current._next
            target._rear = previous
            target._count = self._count
        return target

    def reverse_pc(self):
        """
        -------------------------------------------------------
        Reverses a list through partitioning and concatenation.
        Use: lst.reverse_pc()
        -------------------------------------------------------
        Returns:
            The contents of the current list are reversed.
        -------------------------------------------------------
        """
        self._front = self._reverse_pc_aux(self._front)

    def _reverse_pc_aux(self, current):
        """
        -------------------------------------------------------
        Auxiliary function for reverse_pc.
        Use: node = self._reverse_pc_aux(node)
        -------------------------------------------------------
        Parameters:
            current - the current node to process (_List_Node)
        Returns:
            result -
          Recursively split_key and concatenate the list until the end
          of the list is reached.
        -------------------------------------------------------
        """
        if current is None:
            result = None
        else:
            head, tail = self._partition(current)
            tail = self._reverse_pc_aux(tail)
            result = self._concantenate(tail, head)
        return result

    def _partition(self, current):
        """
        -------------------------------------------------------
        Partitions a list at the current node.
        -------------------------------------------------------
        Parameters:
          current - the current node to process
        Parameters:
          current - a valid node dictionary
        Returns:
          Partition a list by removing the first node as 'head' and
          naming the remainder of the list 'tail'. 'node' cannot be None.
        -------------------------------------------------------
        """
        tail = current._next
        head = current
        head._next = None
        return head, tail

    def _concantenate(self, tail, head):
        """
        -------------------------------------------------------
        [function description]
        -------------------------------------------------------
        Parameters:
          head - the head node of a list
          tail - the tail node of a list
        Parameters:
          head - a valid node dictionary
          tail - a valid node dictionary
        Returns:
         Appends the 'head' node to the end of 'tail'.
        -------------------------------------------------------
        """
        previous = None
        current = tail

        # Find the end of 'tail'.
        while current is not None:
            previous = current
            current = current._next

        # Append 'head' to the end of 'tail'.
        if previous is None:
            tail = head
        else:
            previous._next = head
        # 'tail' is the new head of the list.
        return tail

    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the front
        of the current List. Private helper method.
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        node._next = self._front
        self._front = node

        if self._rear is None:
            # Target list is empty
            self._rear = node
        self._count += 1
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node

        node._next = None
        self._rear = node
        self._count += 1
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        while source1._front is not None and source2._front is not None:
            self._move_front_to_rear(source1)
            self._move_front_to_rear(source2)

        if source1._front is not None:
            self._append_list(source1)

        if source2._front is not None:
            self._append_list(source2)
        return

    def _append_list(self, source):
        """
        -------------------------------------------------------
        Appends the entire source list to the rear of the target list.
        The source list becomes empty.
        Use: target._append_list(source)
        -------------------------------------------------------
        Parameters:
            source - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty list"

        node = source._front
        # Update the target queue
        if self._rear is None:
            # Current queue is empty.
            self._front = node
        else:
            self._rear._next = node
        self._rear = source._rear
        self._count += source._count
        # Empty the source queue.
        source._front = None
        source._rear = None
        source._count = 0
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next

    def is_identical_r(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        (recursive version)
        Use: b = source.is_identical_r(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values as
                target in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != target._count:
            identical = False
        else:
            identical = self.is_identical_r_aux(self._front, target._front)
        return identical

    def is_identical_r_aux(self, node1, node2):
        """
        -------------------------------------------------------
        An auxiliary function for is_identical_r
        -------------------------------------------------------
        Parameters:
            node1 - a List node (_ListNode)
            node2 - a List node (_ListNode)
        Returns:
            identical - True if node1 contains the same values as node2
                in the same order, otherwise False.
        -------------------------------------------------------
        """
        if node1 is None:
            identical = True
        elif node1._value != node2._value:
            identical = False
        else:
            identical = self.is_identical_r_aux(node1._next,
                                                node2._next)
        return identical

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target1, target2 = source.split_alt_r()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        even = List()
        odd = List()
        self._split_alt_r_aux(even, odd)
        return even, odd

    def _split_alt_r_aux(self, even, odd):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd numbered elements.
        Order of even and odd is not significant.
        -------------------------------------------------------
        Parameters:
            even - the even numbered elements of the source list (List)
            odd - the odd numbered elements of the source list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._front is not None:
            even._move_front_to_rear(self)
            # Reverse the order of the arguments.
            self._split_alt_r_aux(odd, even)
        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection_r(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._intersection_r_aux(source2, source1._front)
        return

    def _intersection_r_aux(self, source2, node1):
        """
        -------------------------------------------------------
        Auxiliary function for intersection_r.
        Use: self._intersection_r_aux(node1, node2)
        -------------------------------------------------------
        Parameters:
            source1 - a List (_ListNode)
            source2 - a List (_ListNode)
        Returns:
            None
        -------------------------------------------------------
        """
        if node1 is not None:
            value = node1._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in new list.
                    self.append(value)
            self._intersection_r_aux(source2, node1._next)
        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union_r(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._union_r_aux(source1._front)
        self._union_r_aux(source2._front)
        return

    def _union_r_aux(self, node):
        """
        -------------------------------------------------------
        Auxiliary function for union_r.
        Use: self._union_r_aux(node)
        -------------------------------------------------------
        Parameters:
            node - right side list rs_node (_ListNode)
        Returns:
            None
        -------------------------------------------------------
        """
        if node is not None:
            _, current, _ = self._linear_search(node._value)

            if current is None:
                # Value does not exist in current list.
                self.append(node._value)
            self._union_r_aux(node._next)
        return

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: source.reverse_r()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self._rear = self._front
        self._front = self._reverse_r_aux(None, self._front)
        return

    def _reverse_r_aux(self, previous, current):
        """
        -------------------------------------------------------
        Auxiliary recursive function for reverse_r.
        Use: previous = self.reverse_r_aux(new_front)
        -------------------------------------------------------
        Parameters:
            previous - the node to link back to (_ListNode)
            current - the node to update the _next link (_ListNode)
        Returns:
            previous - the last node linked to
        -------------------------------------------------------
        """
        if current is not None:
            temp = current._next
            current._next = previous
            previous = self._reverse_r_aux(current, temp)
        return previous

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search_r(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        previous, current, index = self._linear_search_r_aux(
            key, None, self._front, 0)
        return previous, current, index

    def _linear_search_r_aux(self, key, previous, current, index):
        """
        -------------------------------------------------------
        Auxiliary method for _linear_search.
        Use: p, c, i = self._linear_search(key, previous, current, index)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        if current is None:
            index = -1
        elif current._value != key:
            previous, current, index = self._linear_search_r_aux(
                key, current, current._next, index + 1)

        return previous, current, index

"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-03-09"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy



class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._front is None:
            new_node = _Deque_Node(value, None, None)
            self._rear = new_node
            self._front = new_node
        else:
            new_node = _Deque_Node(value, None, self._front)
            self._front = new_node
            
        self._count += 1
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _Deque_Node(value, self._rear, None)
        if self._front is None:          
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
            
        self._count += 1
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"
        
        value = self._front
        self._front = self._front._next
        
        self._count -= 1
        if self._count == 0:
            self._rear = None
        else:
            self._front._prev = None
        return value._value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"

        value = self._rear
        self._rear = self._rear._prev
        
        self._count -= 1
        if self._count == 0:
            self._front = None
        else:
            self._rear._next = None
        return value._value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"

        value = deepcopy(self._front._value)
        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"

        value = deepcopy(self._rear._value)
        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"
        if l!=r:
            # one is front
            if (self._front == l or self._front == r) and (self._rear != l and self._rear != r):
                front, n = self._determine_front(l, r)
                temp_prev = None
                temp_next = front._next
                front._next._prev = n
                front._prev = n._prev
                front._next = n._next
                n._prev._next = front
                n._next._prev = front
                n._prev = temp_prev
                n._next = temp_next
                self._front = n
            # one is rear
            elif self._rear == l or self._rear == r and self._front != l and self._front != r:
                rear, n = self._determine_rear(l, r)
                temp_prev = rear._prev
                temp_next = None
                rear._prev._next = n
                rear._prev = n._prev
                rear._next = n._next
                n._prev._next = rear
                n._next._prev = rear
                n._prev = temp_prev
                n._next = temp_next
                self._rear = n
            #head and rear
            elif (self._front==l and self._rear==r) or (self._front==r and self._rear==l):
                front,rear = self._determine_front(l, r)
                temp_prev = None
                temp_next = front._next
                front._next._prev = rear
                front._prev = rear._prev
                front._next = None
                rear._prev._next = front
                rear._prev = temp_prev
                rear._next = temp_next
                self._front = rear
                self._rear = front
            #adjacent nodes
            elif (r._next==l and l._prev == r) or (l._next == r and r._prev==l):
                b,c = self._determine_closer_to_front(l, r)
                temp_prev = b._prev
                b._prev._next = c
                b._next = c._next
                b._prev = c
                c._next._prev = b
                c._next = b
                c._prev = temp_prev
                
            #internal nodes and not adjacent
            else:
                temp_prev = l._prev
                temp_next = l._next
                l._next._prev = r
                l._prev._next = r
                l._prev = r._prev
                l._next = r._next
                r._prev._next = l
                r._next._prev = l
                r._prev = temp_prev
                r._next = temp_next
        return

    def _determine_front(self, l, r):
        '''
        given two nodes return which one is the front
        Returns:
            value - the front node
            n - the other node
        '''
        if self._front == l:
            value = l
            n = r
        else:
            value = r
            n = l
        return value, n
    
    def _determine_rear(self, l, r):
        '''
        given two nodes return which one is the rear
        '''
        if self._rear == l:
            value = l
            n = r
        else:
            value = r
            n = l
        return value, n
    
    def _determine_closer_to_front(self,l,r):
        '''
        given two nodes determine which one has a lower index
        '''
        l_index = 0
        r_index = 0
        current = self._front
        while current !=l:
            l_index+=1
            current = current._next
            
        current = self._front
        while current !=r:
            r_index+=1
            current = current._next
            
        if r_index<l_index:
            value = r
            n = l
        else:
            value = l
            n = r
        return value,n
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
        
    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


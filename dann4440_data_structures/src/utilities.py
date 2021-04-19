"""
-------------------------------------------------------
[Utilities]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-21"
-------------------------------------------------------
"""
from Food import Food
from Stack_array import Stack
from Priority_Queue_array import Priority_Queue
from Queue_array import Queue
from List_array import List


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        stack.push(source.pop(-1))
    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not stack.is_empty():
        target.insert(0, stack.pop())
    
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()   
    empty_before = s.is_empty()
    s.push(source[1])
    empty_after = s.is_empty()
    n = s.peek()
    p = s.pop()
    empty_end = s.is_empty()
    
    print(s)
    print("the initial stack is empty: {}".format(empty_before))
    print("After pushing a value is_empty should be false: {}".format(empty_after))
    print("The value pushed to the stack is {}".format(n))
    print("Pop that value: {}".format(p))
    print("Now the stack is empty again {}".format(empty_end))
    print(s)
    return 


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    l = len(source)
    while i < l:
        queue.insert(source.pop(0))
        i += 1
    return  


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())
    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    l = len(source)
    while i < l:
        pq.insert(source.pop(0))
        i += 1
    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return

    
def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    print("The queue is empty: ", q.is_empty())
    print("The length should be 0:", len(q))
    q.insert(a[0])
    print("Is empty should now be false: ", q.is_empty())
    print("The length should now be 1: ", len(q))
    p = q.peek()
    print("The value added and peeked is:")
    print(p)
    r = q.remove()
    print("remove the value: ", r)
    print("Empty again: ", q.is_empty())

    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    print("The p queue is empty: ", pq.is_empty())
    pq.insert(a[0])
    print("Is empty should now be false: ", pq.is_empty())
    p = pq.peek()
    print("The value added and peeked is:", p)
    pq.insert(a[1])
    p = pq.peek()
    print("The value added is:")
    print(a[1])
    print("and the value next up is:")
    print(p)
    r = pq.remove()
    print("remove the value: ", r)

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        llist.append(source.pop(0))
    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not llist.is_empty():
        target.append(llist.pop(0))
    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    print("the list should be empty",lst.is_empty())
    lst.append(source[0])
    print("is empty false now:",lst.is_empty())
    print()
    print("append and peek the value", lst.peek())
    print()
    lst.append(source[1])
    lst.insert(0,source[2])
    print("insert a food at index 0")
    print()
    for v in lst:
        print(v)
    print()
    print("What is the maximum food?",lst.max())
    print()
    print("What is the minimum food?",lst.min())
    print()
    key = Food("Spring rolls wrong", 2, True, 653)
    print("find any instances spring rolls wrong:")
    print("does it contain key?",key in lst)
    print("how many times?",lst.count(key))
    
    r = lst.remove(key)
    print("remove spring rolls wrong",r)
    print()
    lst[1] = Food("Chickie Nuggies",1,False,66)
    hmm = lst[0]
    print("update the list at index 1")
    print("the first variable in the list is",hmm)
    for v in lst:
        print(v)
    n = lst.index(Food("Chickie Nuggies",1,False,66))
    print("the index Chickie Nuggies is",n)
    print()
    print("finding chickie nuggies...")
    print(lst.find(Food("Chickie Nuggies",1,False,66)))
    
    return

def has_balanced_brackets(s):
    """
    -------------------------------------------------------
    Determines whether a string contains balanced brackets or not.
    Must use a Stack to do so.
    Use: b = balanced_brackets(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        balanced - True if s contains balanced brackets, False otherwise (boolean)
    -------------------------------------------------------
    """
    brackets_stack = Stack()
    brackets_match = True
    OPEN_BRACKETS = "([{"
    CLOSE_BRACKETS = ")]}"
    i=0
    while brackets_match and i<len(s):
        if s[i] in CLOSE_BRACKETS and brackets_stack.is_empty():
            brackets_match = False
        elif s[i] in OPEN_BRACKETS:
            brackets_stack.push(s[i])
        elif s[i] in CLOSE_BRACKETS:
            temp = brackets_stack.pop()
            if OPEN_BRACKETS.find(temp) != CLOSE_BRACKETS.find(s[i]):
                brackets_match = False
        
        i+=1
    if not brackets_stack.is_empty():
        brackets_match = False
    return brackets_match

def total_priority(pq):
    """
    -------------------------------------------------------
    Returns the total priority of all elements of a priority queue.
    Use: n = total_priority(pq)
    -------------------------------------------------------
    Parameters:
        pq - a priority queue with integer priorities (PriorityQueue)
    Returns:
        n - the sum of all priority values in pq (int)
    -------------------------------------------------------
    """
    total = 0 
    priority_tracker = 1
    for i in range(len(pq)):
        total+=priority_tracker
        priority_tracker+=1
    return total
"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-04-01"
-------------------------------------------------------
"""
# Imports
from random import randint
from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100 # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    values = List()
    for i in range(SIZE):
        temp_num = Number(i)
        values.append(temp_num)

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    for i in range(SIZE-1,-1,-1):
        temp_num = Number(i)
        values.append(temp_num)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    lists = []
    for i in range(TESTS):
        temp = List()
        for j in range(SIZE):
            temp.append(Number(randint(0,XRANGE)))
            
        lists.append(temp)

    return lists



def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    sorted = create_sorted()
    reversed = create_reversed()
    rand = create_randoms()
    
    func(sorted)
    comps1 = round(Number.comparisons,0)
    swaps1 = round(Sorts.swaps,0)
    Number.comparisons = 0
    Sorts.swaps = 0
    
    func(reversed)
    comps2 = round(Number.comparisons,0)
    swaps2 = round(Sorts.swaps,0)
    Number.comparisons = 0
    Sorts.swaps = 0
    
    for i in rand:        
        func(i)
    comps3 = round(Number.comparisons//TESTS,0)
    swaps3 = round(Sorts.swaps//TESTS,0)
    Number.comparisons = 0
    Sorts.swaps = 0
    
    print("{:14} {:8} {:8} {:8} {:8} {:8} {:8}".format(title,comps1,comps2,comps3,swaps1,swaps2,swaps3))

    return

print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

test_sort(SORTS[0][0],SORTS[0][1])
test_sort(SORTS[1][0],SORTS[1][1])
test_sort(SORTS[2][0],SORTS[2][1])
test_sort(SORTS[3][0],SORTS[3][1])
test_sort(SORTS[4][0],SORTS[4][1])


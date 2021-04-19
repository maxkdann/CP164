
"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-21"
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array, stack_test
from Food_utilities import read_foods
from Food import Food
def main():
    '''
    s = Stack()
    arr = [11, 22, 33, 44, 55, 66]
    array_to_stack(s, arr)
    for v in s:
        print(v)
    stack_to_array(s,arr)
    print(arr)
    '''
    
    '''
    arr2 = [1,2,3,4]
    s2 = Stack()
    for a in arr2:
        s2.push(a)
    stack_test(s2)
    for v in s2:
        print(v)
    '''
    #testing the stack
    arr2 = [1,2,3,4]
    stack_test(arr2)
    
    f = Food("bread",10,True,55)
    g = Food("grape",6,False,9)
    foods = [f,g]
    stack_test(foods)
    '''
    fv = open("foods.txt","r",encoding = "utf-8")
    foods = read_foods(fv)
    stack_test(foods)
    '''
main()
"""
-------------------------------------------------------
[t1]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-29"
-------------------------------------------------------
"""
from Stack_array import Stack
from functions import stack_split_alt
def main():
    s = Stack()
    l = [1,2,3,4,5,6]
    
    for v in l:
        s.push(v)
    target1,target2 = stack_split_alt(s)
    print(target1)
    print(target2)
main()
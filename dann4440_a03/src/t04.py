"""
-------------------------------------------------------
[t04]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-30"
-------------------------------------------------------
"""
from Stack_array import Stack
def main():
    source1 = Stack()
    source2 = Stack()
    l = [8,12,8,5]
    for v in l:
        source1.push(v)
    l2 = [14,9,7,1,6,3]
    for x in l2:
        source2.push(x)
    stack = Stack()
    stack.combine(source1, source2)
    for s in stack:
        print(s)
main()
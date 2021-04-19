"""
-------------------------------------------------------
[t03]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-05"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
def main():
    pq = Priority_Queue()
    pq.insert(99)
    print(pq._values)
    target1, target2 = pq.split_key(100)
    
    print(target1._values)
    print(target2._values)
    
main()
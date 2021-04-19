"""
-------------------------------------------------------
[t05]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-06"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
def main():
    pq = Priority_Queue()
    pq.insert(2)
    pq.insert(5)
    pq.insert(26)
    pq.insert(22)
    pq.insert(3)
    print(pq._values)
    target1,target2 = pq.split_alt()
    print(target1._values)
    print(target2._values)
    
main()
"""
-------------------------------------------------------
[t02]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-04"
-------------------------------------------------------
"""
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue
def main():
    pq = Priority_Queue()
    pq.insert(10)
    pq.insert(1)
    pq.insert(4)
    pq.insert(7)
    pq.insert(11)
    target1,target2 = pq_split_key(pq, 6)
    
    for t in target1:
        print(t)
    print()
    for v in target2:
        print(v)
        
    
main()
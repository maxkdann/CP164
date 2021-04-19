"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-28"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
def main():
    pq = Priority_Queue()
    pq.insert(3)
    pq.insert(2)
    r = pq.remove()
    print(r)
    
main()
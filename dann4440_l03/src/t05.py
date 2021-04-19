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
from Queue_array import Queue
from utilities import array_to_queue
def main():
    q = Queue()
    source = [1,2,3]
    array_to_queue(q, source)
    for v in q:
        print(v)
    
main()
"""
-------------------------------------------------------
[t06]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-06"
-------------------------------------------------------
"""
from utilities import array_to_list,list_to_array
from List_array import List
def main():
    llist = List()
    source = [1,2,3]
    array_to_list(llist, source)
    for v in llist:
        print(v)
    target = []
    list_to_array(llist, target)
    print(target)
main()
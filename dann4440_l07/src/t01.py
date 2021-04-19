"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-03-03"
-------------------------------------------------------
"""
from List_linked import List
l = List()
l.append(1)
l.append(3)


p,c,i = l._linear_search_r(3)
print("recursively there is a 3 found at index:",i)
"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-24"
-------------------------------------------------------
"""
from List_linked import List
l = List()
l.append(5)
l.append(99)
l.remove(99)
for v in l:
    print(v)
    
print(l[0])
l[0] = 66
print(l[0])
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
l.append(2)
l.append(3)
for i in l:
    print(i)
l.reverse_r()
print()
for j in l:
    print(j)
print()
print(l._rear._value)
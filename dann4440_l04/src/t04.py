"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-05"
-------------------------------------------------------
"""
from List_array import List
def main():
    
    l = List()
    '''
    p = [2,3]
    i = p.index(3)
    print(i)
    '''
    l.append(2)
    l.append(3)
    l.append(1)
    
    i2 = l.index(3)
    print(i2)
    
    f = l.find(2)
    print(f)
    
    b = 2
    c = 34
    print(b in l)
    print(c in l)
    
    print(l.count(2))
    print(l.count(34))
    
    print(l.min())
    print(l.max())
main()

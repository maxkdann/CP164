"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-03-22"
-------------------------------------------------------
"""
from Hash_Set_array import Hash_Set
from Food_utilities import read_foods
fv = "foods.txt"
f = open(fv,"r",encoding = "utf-8")
foods = read_foods(f)
h = Hash_Set(3)
l = [1,2,3,4,5,4,6,7,8,9,10]
for f in l:
    h.insert(f)
    

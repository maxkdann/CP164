"""
-------------------------------------------------------
[t07]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-05"
-------------------------------------------------------
"""
from utilities import list_test
from Food import Food
def main():
    f1 = Food("not spring rolls",1,False,66)
    f2 = Food("spring rolls wrong",2,True,653)
    f3 = Food("good spring rolls",1,True,7)
    source = [f1,f2,f3]
    source2 = [6,8,2]
    list_test(source)
    
main()
"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-29"
-------------------------------------------------------
"""
from utilities import queue_test
from Food_utilities import read_foods
def main():
    fv = open("foods.txt","r",encoding = "utf-8")
    foods = read_foods(fv)
    queue_test(foods)
    
main()
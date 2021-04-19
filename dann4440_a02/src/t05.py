"""
-------------------------------------------------------
[t05]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-23"
-------------------------------------------------------
"""
from Food_utilities import food_search
from Food import Food
def main():
    food = Food("grape",3,True,5)
    food1 = Food("chicken",2,False,67)
    food2 = Food("sushi",3,True,10)
    food3 = Food("water",3,True,0)
    foods = [food,food1,food2,food3]
    result = food_search(foods, -1, 0, True)
    
    for f in result:
        print(f)
        
main()
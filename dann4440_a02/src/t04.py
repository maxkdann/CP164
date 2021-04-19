"""
-------------------------------------------------------
[t04]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-23"
-------------------------------------------------------
"""
from Food_utilities import food_table
from Food import Food
def main():
    food = Food("BBQ Pork",1,False,920)
    food1 = Food("Beef with Green Pepper",1,False,251)
    foods = [food1,food]
    food_table(foods)
    #print(food1.name)
main()
"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-14"
-------------------------------------------------------
"""

from Food import Food
from Food_utilities import write_foods,read_foods, read_food, by_origin, average_calories, get_food
food = Food("grape",3,True,67)
#test 1
#print(Food.origins())

#test 2
#print(food)

#test 3
'''
f = get_food()
print(f)
'''

#test 4
'''
f = read_food("Spanakopita|5|True|260")
print(f)
'''

#test 5
'''
file_name = "foods.txt"
fv = open(file_name,"r",encoding = "utf-8")
foods = read_foods(fv)
'''

#test 6
'''
fn = "foods.txt"
fv = open(fn,"w",encoding = "utf-8")

write_foods(fv, foods)
'''

#test 7
'''
v = get_vegetarian(foods)
'''
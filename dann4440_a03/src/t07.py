"""
-------------------------------------------------------
[t07]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-30"
-------------------------------------------------------
"""
from functions import stack_maze
def main():
    maze = {'Start': ['A'], 'A':['C', 'B'], 
            'B':[], 'C':['D', 'X']}
    path = stack_maze(maze)
    print(path)
main()
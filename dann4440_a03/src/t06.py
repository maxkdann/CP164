"""
-------------------------------------------------------
[t06]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-30"
-------------------------------------------------------
"""
from functions import postfix
def main():
    string = "4 5.2 + "
    answer = postfix(string)
    print(answer)
main()
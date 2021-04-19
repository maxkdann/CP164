"""
-------------------------------------------------------
[t10]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-14"
-------------------------------------------------------
"""
from functions import pig_latin
def main():
    word = input("Word: ")
    out = pig_latin(word)
    print("Pig-Latin: {}".format(out))
    
main()
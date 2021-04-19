"""
-------------------------------------------------------
[t09]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-14"
-------------------------------------------------------
"""
from functions import dsmvwl
def main():
    s = input("Enter a sentence: ")
    out = dsmvwl(s)
    print("Disemvowelled: {}".format(out))
main()
"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-03-24"
-------------------------------------------------------
"""

from BST_linked import BST
from Letter import fill_letter_bst
from functions import do_comparisons, comparison_total, letter_table
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"


bst2 = BST()


fill_letter_bst(bst2, DATA2)


letter_table(bst2)

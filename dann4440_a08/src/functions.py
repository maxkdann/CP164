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
from Letter import Letter
def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    line = file_variable.readline()
    lines = []
    while line !="":
        line = line.strip()
        lines.append(line)
        line = file_variable.readline()
    for line in lines:
        for letter in line:
            if letter.isalpha():
                temp_letter = Letter(letter.upper())
                bst.retrieve(temp_letter)
    file_variable.close()
    return
    
def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    a = bst.inorder()
    total = 0
    for letter in a:
        total+=letter.comparisons
    return total

def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    letters = bst.inorder()
    total = 0
    for l in letters:
        total+=l.count
    
    print("Letter Count/Percent Table")
    print()
    print("Total Count: {:,}".format(total))
    print()
    print("Letter  Count       %")
    print("---------------------")
    for l in letters:
        per = l.count/total*100
        print("{:>4s}{:>7,d}{:9.2f}%".format(l.letter,l.count,per))
    
    return
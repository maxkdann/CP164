"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-03-31"
-------------------------------------------------------
"""
from Word import Word


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in fv and inserts into
    a Hash_Set.
    Each Word object in hash_set contains the number of comparisons
    required to insert that Word object from file_variable into hash_set.
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    
    fv.seek(0)


    for line in fv:
        for word in line.strip().split():
            
            if word.isalpha():
                l = Word(word.lower())
                hash_set.insert(l)
                
    fv.close()
    return

    
def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_word = Word("a")
    for slot in hash_set._table:
        for item in slot:
            total+=item.comparisons
            if item.comparisons>max_word.comparisons:
                max_word = item
    
    return total,max_word
    

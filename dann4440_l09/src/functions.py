"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-03-17"
-------------------------------------------------------
"""
def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
    1652346    3 Dark City, 1998
    848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots,values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hashes")
    print("Hash     Slot Key")
    print("======== ==== ====================")
    for i in values:
        h = hash(i)
        slot = h%7
        f_str =  i.key()
        print("{:8}{:5} {}".format(h,slot,f_str))
    return
    



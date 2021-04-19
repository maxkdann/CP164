"""
-------------------------------------------------------
[A1 functions file]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-09"
-------------------------------------------------------
"""

def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a (int)
    -------------------------------------------------------
    """
    if len(a)>0:
        md = a[0]
        for i in range(len(a)-1):
            if a[i+1]-a[i]>md:
                md = a[i+1]-a[i]
    else:
        md = 0
    return md

def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = True
    if name[0].isalpha()==False and name[0]!="_":
        valid = False
    else:
        for i in name:
            if i.isalnum() == False and i!="_":
                valid = False
    return valid

def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = a[0][0]
    large = a[0][0]
    total = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]<small:
                small = a[i][j]
            if a[i][j]>large:
                large = a[i][j]
            total+=a[i][j]
    average = total/(len(a)*len(a[0]))
    return small,large,total,average

def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a. A 'flattened' list is a
    2D list that is converted into a 1D list.
    a must be unchanged.
    Use: b = matrix_flatten(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """
    b = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            b.append(a[i][j])
    return b

def matrixes_add(a, b):
    """
    -------------------------------------------------------
    Sums the contents of matrixes a and b. a and b must have
    the same number of rows and columns.
    a and b must be unchanged.
    Use: c = matrixes_add(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix sum of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    c = a
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j] = (a[i][j]+b[i][j])
    return c

def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = [[0]*len(b[0]) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k]*b[k][j]
    return c

def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    b = [[0]*len(a) for i in range(len(a[0]))]
    for j in range(len(a)-1,-1,-1):
        for i in range(len(a[0])):
            b[i][j] = a[j][i]
    for i in range(len(b)):
        b[i] = b[i][::-1]
    return b

def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    data = []
    line = fv.readline()
    while line!="":
        data.append(line.strip())
        line = fv.readline()
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j].isupper():
                u+=1
            elif data[i][j].islower():
                l+=1
            elif data[i][j].isdigit():
                d+=1
            elif data[i][j] == " ":
                w+=1
            else:
                r+=1
    return u,l,d,w,r

def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    out = ""
    VOWELS = ["a","e","i","o","u","A","E","I","O","U"]
    for c in s:
        if c not in VOWELS:
            out+=c
    return out

def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    VOWELS = ["a","e","i","o","u","A","E","I","O","U"]
    pl = ""
    #check case
    upper = False
    if word[0].isupper():
        upper = True
    if word[0] in VOWELS:
        pl+=word+"way"
    else:
        VOWELS_AND_Y = ["a","e","i","o","u","A","E","I","O","U","y","Y"]
        c = []
        if word[0]=="y"or word[0]=='Y':
            word = word[1:]+word[0].lower()
        w = 0
        while word[w] not in VOWELS_AND_Y:
            c.append(word[w].lower())
            w+=1
        pl = word[len(c):]
        for i in c:
            pl+=i
        pl+="ay"
    if upper:
        pl = pl[0].upper()+pl[1:]
    return pl
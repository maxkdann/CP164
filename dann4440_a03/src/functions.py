"""
-------------------------------------------------------
[functions]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-01-29"
-------------------------------------------------------
"""
from Stack_array import Stack


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = []
    target2 = []
    i = 1
    while not source.is_empty():
        if i % 2 != 0:
            target1.append(source.pop())
        else:
            target2.append(source.pop())
        i += 1
    return target1, target2


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    both_empty = source1.is_empty() and source2.is_empty()
    i = 1
    while not both_empty:
        if i % 2 != 0:
            if not source1.is_empty():
                target.push(source1.pop())
            else:
                target.push(source2.pop())
        else:
            if not source2.is_empty():
                target.push(source2.pop())
            else:
                target.push(source1.pop())
        i += 1
        both_empty = source1.is_empty() and source2.is_empty()
    return target


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    chars = ""
    for s in string:
        if s.isalpha():
            chars += s.lower()
            
    l = len(chars)
    mid = -1
    if l == 0:
        palindrome = True
    else:
        mid = l // 2
        first_half = Stack()
        for i in range(mid):
            first_half.push(chars[i])
        if l % 2 == 0:
            second_half_chars = chars[mid:]
        else:
            second_half_chars = chars[mid + 1:]
        second_half_chars = second_half_chars.lower()  
        i = 0
        while palindrome and i < mid:
            s = second_half_chars[i]
            p = first_half.pop()
            if s == p:
                i += 1
            else:
                palindrome = False
    return palindrome


# Constants
OPERATORS = "+-*/"
NUMBERS = "12356890"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    elements = string.split()
    for e in elements:
        if e not in OPERATORS:
            stack.push(e)
        else:
            top = float(stack.pop())
            second = float(stack.pop())
            if e=="+":
                stack.push(second+top)
            elif e == "-":
                stack.push(second-top)
            elif e =="*":
                stack.push(second*top)
            else:
                stack.push(second/top)
    answer = stack.pop()
    return answer

def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    try:
        current = "Start"
        choices = maze[current]
        path = []
        if "X" in choices:
            path.append("X")
        stack = Stack()
        while "X" not in choices:
            for c in choices:
                stack.push(c)
            current = stack.pop()
            if maze[current]!=[]:
                path.append(current)          
            choices = maze[current]
            if "X" in choices:
                path.append("X")
    except:     
        path = None
    finally:
        return path
"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))
"""

# comment code with instance creation i stack_ex.py file
from stack_ex import Stack

def is_match(p1, p2):
    return (p1 == "(" and p2 == ")") or (p1 == "[" and p2 == "]") or (p1 == "{" and p2 == "}")

def is_parentesis_balanced(str):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(str) and is_balanced:
        parethesis = str[index]
        if parethesis in "{[(":
            s.push(parethesis)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, parethesis):
                    is_balanced = False
        index = index + 1
    return s.is_empty() and is_balanced

print(is_parentesis_balanced("([])"))
# prosiriti zadataka da radi sa brojevima
# stack_ex.py should contain the Stack class used here.

from stack_ex import Stack

def is_match(p1, p2):
    return (p1 == "(" and p2 == ")") or (p1 == "[" and p2 == "]") or (p1 == "{" and p2 == "}")

def is_parenthesis_balanced(string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(string) and is_balanced:
        char = string[index]
        if char.isdigit():  # Ignore numbers
            index += 1
            continue
        if char in "{[(":
            s.push(char)
        elif char in "}])":
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, char):
                    is_balanced = False
        index += 1
    return s.is_empty() and is_balanced

# Testing with examples that contain numbers
print(is_parenthesis_balanced("([])"))            # True, balanced
print(is_parenthesis_balanced("(3[2]{1})"))       # True, balanced
print(is_parenthesis_balanced("(3[2]{1)(4"))      # False, not balanced
print(is_parenthesis_balanced("({[123]})"))       # True, balanced
print(is_parenthesis_balanced("{[5]}"))           # True, balanced
print(is_parenthesis_balanced("{[}]"))            # False, not balanced

"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
>>> print(backspace_compare("ab#c", "ad#c"))
True
"""


def backspace_method(s: str):
    # a method that finds '#' and applies a backspace
    i = 0
    while i < len(s):
        if s[i] == '#':
            if i == 0:
                s = s[1:]
            else:
                s = s[:i - 1] + s[i + 1:]
                i = 0
        i += 1
    return s


def backspace_compare(first: str, second: str):
    new_first = backspace_method(first)
    new_second = backspace_method(second)
    if new_first == new_second:
        return True
    else:
        return False

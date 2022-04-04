import doctest
from typing import Union, Type

"""
This function reads the file and checks the values in the file
returns: true if 1<= values < 3 in the file, otherwise false or 
ValueError if the values in the file are not a number.

"""


def read_magic_number(path: str) -> Union[bool, Type[ValueError]]:
    """
    >>> read_magic_number("files/file_true.txt")
    True
    >>> read_magic_number("files/file_false.txt")
    False
    >>> read_magic_number("files/file_error.txt")
    <class 'ValueError'>
    """
    with open(path) as file:
        result = True
        try:
            line_number: list[str] = file.readline().split()
            for i in range(0, len(line_number)):
                if 1.0 <= float(line_number[i]) < 3.0:
                    pass
                else:
                    return False
        except ValueError:
            return ValueError

        return result


if __name__ == '__main__':
    doctest.testmod()

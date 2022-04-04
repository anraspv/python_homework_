import sys
import doctest

"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.
"""


def my_precious_logger(text: str):
    """
    >>> my_precious_logger("error: file not found")
    'error: file not found'
    >>> my_precious_logger("OK")
    'OK'
    """
    line_stderr = sys.stderr
    line_stdout = sys.stdout
    if text.split()[0] == 'Error:':
        line_stderr.write(text + '\n')
    else:
        line_stdout.write(text + '\n')


if __name__ == '__main__':
    doctest.testmod()

import doctest
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(8)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8']
    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']

    :param n: numbers 1 to n
    :return: List[str] where each el % 3 == 0 = fizz and each el % 5 == 0 = buzz
    if el % 15 == 0 = fizzbuzz
    """
    list_fb: List[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            list_fb.append("fizzbuzz")
        elif i % 3 == 0:
            list_fb.append("fizz")
        elif i % 5 == 0:
            list_fb.append("buzz")
        else:
            list_fb.append(f"{i}")

    return list_fb


if __name__ == '__main__':
    doctest.testmod()

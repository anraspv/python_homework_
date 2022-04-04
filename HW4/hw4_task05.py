import doctest
from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """
    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']
    >>> list(fizzbuzz(8))
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8']
    >>> list(fizzbuzz(15))
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']

    :param n: numbers 1 to n
    :return: List[str] where each el % 3 == 0 = fizz and each el % 5 == 0 = buzz
    if el % 15 == 0 = fizzbuzz
    """
    for i in range(1, n + 1):
        yield "fizz" * (not i % 3) + "buzz" * (not i % 5) or str(i)


if __name__ == '__main__':
    doctest.testmod()

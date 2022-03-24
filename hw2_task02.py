"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable
from functools import lru_cache


def cache(func: Callable) -> Callable:
    """
 we use the caching function (decorator) lru_cache.
 lru_cache provides a cache of the latest results of the execution of functions,
 or in other words, remembers the result of their work:
    """

    @lru_cache
    def inner(*args):
        return func(*args)

    return inner


# for example
# passing a function with arguments a and b
def func(a, b):
    return (a ** b) ** 2


# decorating our function
cache_func = cache(func)

some = 2, 3

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

print(val_1)
print(val_2)
"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contain basic structures like:
    str, list, tuple, dict, set, int, bool
>>> find_occurrences(example_tree, "RED") == 6
True
"""
from typing import Any
import itertools

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    def counter(dictionary, elem):
        for value in (dictionary.values() if isinstance(dictionary, dict) else dictionary):
            """
            we generate a list consisting of the desired element.
            Since the value can be str, list, tuple, dict, set, int, bool, then 
            we are considering different options for generating a list from the desired element.
            at the end, we output the number of items in the resulting list.
            """
            if value == elem:
                yield value
            elif isinstance(value, (list, tuple, set)):
                yield from counter(value, elem)
            elif isinstance(value, dict):
                yield from counter(value.values(), elem)
    return len(list(counter(tree, element)))

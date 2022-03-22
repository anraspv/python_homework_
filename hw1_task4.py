"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def zeros_from_four_lists(a: List[int], b: List[int], c: List[int], d: List[int]) -> List[tuple]:
    list_of_proper_indexes = []
    n = len(a)
    for i in range(0, n-1):
        for j in range(0, n-1):
            for k in range(0, n-1):
                for m in range(0, n-1):
                    sum_of_elements = a[i] + b[j] + c[k] + d[m]
                    if sum_of_elements == 0:
                        list_of_proper_indexes.append((i, j, k, m))
    return list_of_proper_indexes
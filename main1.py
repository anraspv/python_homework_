import hw1_task4

import hw1_task5

import random

"""
N = random.randint(0, 100)
A = []
B = []
C = []
D = []

for i in range(0, N):
    A.append(random.randint(-500, 500))
    B.append(random.randint(-500, 500))
    C.append(random.randint(-500, 500))
    D.append(random.randint(-500, 500))

result = hw1_task4.zeros_from_four_lists(A, B, C, D)
print(f"that's how many tuples we found: {len(result)}")
print("here are all of them: ")
for tup in result:
    print(tup)
"""
#---------------------------------------------------------------------
nums = [1, 3, -1, -3, 5, 3, 6, 7]
print(hw1_task5.find_maximal_subarray_sum(nums, 3))


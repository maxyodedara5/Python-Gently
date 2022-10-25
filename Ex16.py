# InventWithPython Exercise number 16

"""
Write a mode() function that has a numbers parameter. 
This function returns the mode, or most frequently appearing number, 
of the list of integer and floating-point numbers passed to the function.
"""
# This doesn't cover the possibility of multiple nodes so skipped 
# Ideally you would return a list if data has multiple nodes

from itertools import count


def mode(numbers):

    if len(numbers) == 0:
        return None
    counts = {}
    for i in numbers:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    cur_value = 0 
    for key,value in counts.items():
        if value > cur_value:
            mode = key
            cur_value = value
            
    return mode


assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4



(print("Ex16 done"))
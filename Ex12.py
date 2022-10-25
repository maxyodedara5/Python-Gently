# InventWithPython Exercise number 12

"""
Write a getSmallest() function that has a numbers parameter. 
The numbers parameter will be a list of integer and floating-point number values. 
The function returns the smallest value in the list. 
If the list is empty, the function should return None. 
Since this function replicates Python’s min() function, your solution shouldn’t use it.
"""

import sys


def getSmallest(numbers):

    if len(numbers) == 0:
        return None

    smallest = sys.maxsize
    for i in numbers:
        if i < smallest :
            smallest = i 
    
    return smallest 

assert getSmallest([1, 2, 3]) == 1

assert getSmallest([3, 2, 1]) == 1

assert getSmallest([28, 25, 42, 2, 28]) == 2

assert getSmallest([1]) == 1

assert getSmallest([]) == None



print("Ex12 done")
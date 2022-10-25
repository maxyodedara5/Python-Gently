# InventWithPython Exercise number 15

"""

Write a median() function that has a numbers parameter. 
This function returns the statistical median of the numbers list. 
The median of an odd-length list is the number in the middlemost number when the 
list is in sorted order. If the list has an even length, the median is the average 
of the two middlemost numbers when the list is in sorted order. 
Feel free to use Python’s built-in sort() method to sort the numbers list.

Passing an empty list to average() should cause it to return None.
"""

def median(numbers):

    if len(numbers) == 0:
        return None

    numbers.sort()
    mid = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[mid]
    else:
        median = (numbers[mid] + numbers[mid-1]) / 2
        return median



assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random

random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6


(print("Ex15 done"))
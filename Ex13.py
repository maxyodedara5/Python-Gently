# InventWithPython Exercise number 13

"""
Write two functions named calculateSum() and calculateProduct(). 
They both have a parameter named numbers, which will be a list of integer or 
floating-point values. The calculateSum() function adds these numbers and returns 
the sum while the calculateProduct() function multiplies these numbers and returns the product. 
If the list passed to calculateSum() is empty, the function returns 0. 
If the list passed to calculateProduct() is empty, the function returns 1. 
Since this function replicates Python's sum() function, your solution shouldn't call.
"""

def calculateSum(numbers):
    if len(numbers) == 0:
        return 0
    
    sum = 0 
    for i in numbers:
        sum += i
    
    return sum

def calculateProduct(numbers):
    if len(numbers) == 0:
        return 1
    
    product = 1
    for i in numbers:
        product *= i
    
    return product

assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840

(print("Ex13 done"))
# InventWithPython Exercise number 17

"""
Write a rollDice() function with a numberOfDice parameter that represents the 
number of six-sided dice. The function returns the sum of all of the dice rolls. 
For this exercise you must import Python's random module to call its random.randint() 
function for this exercise.
"""

import random


def rollDice(numberOfDice):
    diceTotal = 0
    for i in range(0, numberOfDice):
        diceTotal += random.randrange(1,7)
        
    return diceTotal
    

assert rollDice(0) == 0

assert rollDice(1000) != rollDice(1000)

for i in range(1000):

    assert 1 <= rollDice(1) <= 6

    assert 2 <= rollDice(2) <= 12

    assert 3 <= rollDice(3) <= 18

    assert 100 <= rollDice(100) <= 600


(print("Ex17 done"))
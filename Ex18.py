# InventWithPython Exercise number 18

"""
Write a function named getCostOfCoffee() that has a parameters named numberOfCoffees 
and pricePerCoffee. Given this information, the function returns the total cost of the 
coffee order. This is not a simple multiplication of cost and quantity, however, 
because the coffee shop has an offer where you get one free coffee for every eight coffees 
you buy.
"""

def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    cost = 0 

    if numberOfCoffees > 8 :
        coffees = numberOfCoffees // 8
        coffees = numberOfCoffees - coffees
        cost = coffees * pricePerCoffee
    else:
        coffees = numberOfCoffees
        cost = coffees * pricePerCoffee
    return cost


assert getCostOfCoffee(7, 2.50) == 17.50

assert getCostOfCoffee(8, 2.50) == 20

assert getCostOfCoffee(9, 2.50) == 20

assert getCostOfCoffee(10, 2.50) == 22.50

 

for i in range(1, 4):

    assert getCostOfCoffee(0, i) == 0

    assert getCostOfCoffee(8, i) == 8 * i

    assert getCostOfCoffee(9, i) == 8 * i

    assert getCostOfCoffee(18, i) == 16 * i

    assert getCostOfCoffee(19, i) == 17 * i

    assert getCostOfCoffee(30, i) == 27 * i




(print("Ex18 done"))
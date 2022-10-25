"""
Write a getChessSquareColor() function that has parameters column and row. 
The function either returns 'black' or 'white' depending on the color at the 
specified column and row. Chess boards are 8 x 8 spaces in size, and the columns 
and rows in this program begin at 0 and end at 7 like in Figure 9-1. 
If the arguments for column or row are outside the 0 to 7 range, the function 
returns a blank string.

Note that chess boards always have a white square in the top left corner.

"""

def getChessSquareColor(x_co , y_co):
    if  x_co not in range(1, 9) or y_co not in range(1, 9):
        return ""

    if ((x_co - 1) + (y_co - 1)) % 2 != 0:
        return "black"
    else:
        return "white"

 



assert getChessSquareColor(1, 1) == 'white'

assert getChessSquareColor(2, 1) == 'black'

assert getChessSquareColor(1, 2) == 'black'

assert getChessSquareColor(8, 8) == 'white'

assert getChessSquareColor(0, 8) == ''

assert getChessSquareColor(2, 9) == ''

print("Ex9 Done")
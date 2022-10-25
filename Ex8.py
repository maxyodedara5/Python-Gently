"""
You will write three functions for this exercise. 
First, write a writeToFile() function with two parameters for the 
filename of the file and the text to write into the file. 
Second, write an appendToFile() function, which is identical to writeToFile()
except that the file opens in append mode instead of write mode. 
Finally, write a readFromFile() function with one parameter for the filename to open. 
This function returns the full text contents of the file as a string
"""

from fileinput import filename


def writeToFile(fileName, text):
    with open(fileName, 'w') as f:
        f.write(text)
    

def appendToFile(fileName, text):
    with open(fileName, 'a') as f:
        f.write(text)

def readFromFile(fileName):
    with open(fileName) as f:
        data = f.read()
    return data


writeToFile('greet.txt', 'Hello!\n')

appendToFile('greet.txt', 'Goodbye!\n')

assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'

print("Ex8 done")
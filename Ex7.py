"""
Write a printASCIITable() function that displays the ASCII number 
and its corresponding text character, from 32 to 126. 
(These are called the printable ASCII characters.)

32 
33 !
34 "
35 #
"""

def printASCIITabe():
    for i in range(32, 127):
        print(f"{i} {chr(i)}")

printASCIITabe()

print("Ex7 done")
# InventWithPython Exercise number 19

"""
Write a generatePassword() function that has a length parameter. 
The length parameter is an integer of how many characters the generated 
password should have. For security reasons, if length is less than 12, 
the function forcibly sets it to 12 characters anyway. The password string 
returned by the function must have at least one lowercase letter, one uppercase letter, 
one number, and one special character. 
The special characters for this exercise are ~!@#$%^&*()_+.
"""
import random


def generatePassword(length):
    if length < 12: 
        length = 12
    
    password = ""
    specials = "~!@#$%^&*()_+"
    characters = "abcdefghijklmnopqrstuvwxyz"

    password += random.choice(specials)
    password += random.choice(characters)
    password += (random.choice(characters)).upper()
    password += str(random.randrange(0,10))

    for i in range(4,length):
        if i % 3 == 0:
            password += str(random.randrange(0,10))
        elif i % 4 == 0:
            password += (random.choice(characters)).upper()
        elif i % 5 == 0:
            password += random.choice(specials)
        else:
            password += random.choice(characters)

    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    return password
    

assert len(generatePassword(8)) == 12

 

pw = generatePassword(14)

assert len(pw) == 14

hasLowercase = False

hasUppercase = False

hasNumber = False

hasSpecial = False

for character in pw:

    if character in "abcdefghijklmnopqrstuvwxyz":
        hasLowercase = True

    if character in "abcdefghijklmnopqrstuvwxyz".upper():
        hasUppercase = True

    if character in "0123456789":
        hasNumber = True

    if character in "~!@#$%^&*()_+":
        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial

(print("Ex19 done"))
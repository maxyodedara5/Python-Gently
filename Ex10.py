# InventWithPython Exercise number 10

"""
Write a findAndReplace() function that has three parameters: 
text is the string with text to be replaced, oldText is the text to be replaced, 
and newText is the replacement text. Keep in mind that this function must be case-sensitive: 
if you are replacing 'dog' with 'fox', then the 'DOG' in 'MY DOG JONESY' won't be replaced.
"""

def findAndReplace(text, oldText, newText):
    #text = text.replace(oldText, newText)
    present = oldText in text
    while(present):
        if oldText in text:
            position = text.find(oldText)
            finaltext = text[0:position] + newText + text[position + len(oldText) :]
        if oldText in finaltext:
            present = True
            text = finaltext
        else:
            present = False

    return finaltext


assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'

assert findAndReplace('fox', 'fox', 'dog') == 'dog'

assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'

assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'

assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'

print("Ex10 done")

#9689911538 
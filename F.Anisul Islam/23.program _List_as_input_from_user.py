from cgitb import text


numofWords = 0
numofLetters = 0
numOfDigits = 0

text = input("Enter a text of nunbers : ") #My name is 123

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numofLetters = numofLetters + 1

    elif x >= '0' and x <= '9':
        numofLetters = numofLetters + 1
    
    elif x >= ' ':
        numofLetters = numofLetters + 1
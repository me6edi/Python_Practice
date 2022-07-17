
'''
statement1 -> if statement
statement2 -> if statement, else statement
statement3 or more -> if statement, elif statement..., else statement

''' 

marks = 64

if marks >= 80:
    print("A+")

elif marks >= 70:
    print("A")

elif marks >= 60:
    print("A-")

elif marks >= 50:
    print("B")

elif marks >= 40:
    print("C")

elif marks >= 33:
    print("D")
else:
    print("Fail")


if 7 > 3:
    if 7 > 5:
        print("Hi")
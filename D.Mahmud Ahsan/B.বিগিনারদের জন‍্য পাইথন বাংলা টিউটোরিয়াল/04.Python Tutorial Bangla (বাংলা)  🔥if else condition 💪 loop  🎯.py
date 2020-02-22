num = 100
if num % 2 == 0:
    print("Even Number")
    print("Thank you")

#Condition

num = input("Please enter a number: ")
num = int (num)
if num % 2 == 0:
    print("Even Number")
    print("Thank You")
else:
    print("Odd Number")
    print("Come again")

# if-elif-else chained condition

num = input("Please enter a number: ")
num = int(num)
if num == 50:
    print("Half century")
elif num == 100:
    print("Century")
elif num > 100:
    print("Century +")
else:
    print("Unknown number")

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
# Logicla operators
#and
#or
num = 7
if num >=3 and num < 5:
    print('3 to 5')

#Compare string
name1 = "Ahsan"
name2 = "ahsan"

if name1.lower() == name2.lower():
    print("Same Name")
else:
    print("Name Doesn't match")

# Not equals to
name = "Steve Jobs"
if name != "Steve Jobs":
    print(name)

# author Mahmud Ahsan

x = 1
print(x)
x +=1
print(x)
x +=1
print(x)
x += 1
print(x)
x += 1
print(x)

# While loop
x = 1
while x <=5:
    print(x)
    x +=1

# infinite loop
# x = 1
# while True:
#     print(x)
#     x = x + 1

# infinite loop
x = 1
while True:
    print(x)
    x = x + 1
    if x > 10:
        break

# Omit even number  1 to 20
x = 0
while x < 20:
    x +=1
    if x % 2 ==0:
        continue
    print(x)

''''
for element in iterable:
    body
'''

sum = 0
for num in range(1, 11):
    print(num)
    sum += num

print("Sum is {sum}".format(sum = sum))

title = "Applae Inc."
for char in title:
    print(char)



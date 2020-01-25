# What is variable
print("Start What is variable:")
print("Hello world")

name = "Mehedi Amin"
age = 20
country = "Bangladesh"

print(name)
print(age)
print(country)

name = "Grocery List"
detail = 'Buy from supershop'
number_of_items = 5
budget = 2500  # USD
amount_of_rice = 1.56  # kg
should_we_by_tody = True

print(name, type(name))
print(detail, type(detail))
print(number_of_items, type(number_of_items))
print(amount_of_rice, type(amount_of_rice))
print(should_we_by_tody, type(should_we_by_tody))

# Comments
print("Start Comments:")

""""
My name is Mehedi Amin
"""
print("Hello world")

# Statements
print("Start Statements:")

name = "Grocery List"
detail = "Buy from supershop"
number_of_items = 5
number_of_ITEMS = 10

print(name, type(detail))
print(detail, type(detail))
print(number_of_items, type(number_of_items))

# Expression
print("Start Expression:")
a = 2
b = a + 2

# Operators
print("Start Operators:")
number_of_items = 5
number_of_items = number_of_items + 2
print(number_of_items)

number_of_items += 2
print(number_of_items)

amount_of_rice = 1.56

amount_of_rice += 2.3
print(amount_of_rice)

number_of_items *= 3
print(number_of_items)
number_of_items /= 3
print(number_of_items, type(number_of_items))

# Type casting
print("Start Type casting:")

number1 = 10
number2 = 2
result = int(number1 / number2)
print(number1, type(number1))
print(number2, type(number2))
print("Result is: ", result, type(result))

## Negative value
print("Start Negative value:")
x = 10
x = -x
print(x)

## Remainder opertor
print("Start Remainder opertor:")
x = 10
y = 2

print(x, y, x % y)

x = 10.0
y = 3.0
print(x, y, x % y)

## Divmod
print("Start Divmod:")
x = 10
y = 3
result = divmod(x, y)
print(result)
print(result[0])
print(result[1])

## Exponential
print("Start Exponential:")
x = 2
result = x ** 4
print(result)

result = pow(2, 4)
print(result)

## String
print("Start String:")

# Accessing string character
title = "Python Course"
title1 = 'C Course'

print(title)
print(title1)
print(title[0], title[1], title[-1], title[-2])
# String operation
print("Start operation:")

name = 'jonathon swift'
print(name.title())
print(name.upper())
print(name.lower())

print("Start string concatenation:")

first_name = "Steve"
last_name = "Jobs"
name = first_name + ' ' + last_name
print(name)

# Newline
print(first_name + '\n' + last_name)

# Whitespace
name = "     Mr. X    "
print('_' + name + '_')
print('_' + name.lstrip() + '_')
print('_' + name.rstrip() + '_')
print('_' + name.strip() + '_')
print('_' + name.lstrip().rstrip() + '_')

# Printing Single and Double Quote
shop_name = "Rahim's Shop"
print(shop_name)

shop_name = 'Rahim"s shop'
print(shop_name)

shop_name = 'Rahim\'s shop'
print(shop_name)

# Matching test at start and at the end
filename = 'bigdata.txt'
print(filename.endswith('.txt'))
print(filename.startswith('bi'))

# Find word in sentence
sentence = "A quick brown fox jumps over the lazy dog"
print(sentence.find('fox'))
print(sentence.find('foxs'))  # -1 the value not found

# Replace text
sentence = "A quick brown fox jumps over the lazy dog"
sentence = sentence.replace('fox', 'tiger')
print(sentence)

# Print separator
x = 'Dhaka'
y = 'Bogra'
z = 'Comilla'

print(x + ' | ' + y + ' | ' + z)
print(x, y, z, sep=' | ')

# String interpolation
# old style
person = '%s\'s age is %d'
print(person % ('Bill', 55))

print()

# New style
person = '{name}\'s age is {age}'
print(person.format(name='Bill', age=55))
print(person.format(name='Steve', age=50))

# Formatted string literal python 3.6+
name = 'Mark'
age = 30
person = f'{name}\'s age is {age}'
print(person)

# Strign slice
name = "Tylor Swift"
print(name[0: 6])
print(name[:6])
print(name[7:])
print(name[7:-1])

# # # Condition
# num = 100
# if num % 2 == 0:
#     print("Even Number")
#     print("Thank You")
#
# num = input("Please enter a number:")
# num = int(num)
# if num % 2 == 0:
#     print("Even Number")
#     print("Thank you")
# else:
#     print("Odd Number")
#     print("Come Again")
#
#
# # elif number
# num = input("please enter a number:")
# num = int(num)
# if num == 50:
#     print("Half Century")
# elif num == 100:
#     print("Centuray")
# elif num > 100:
#     print("Century +")
# else:
#     print("Unknown number")

# Logical operators and,or,not
num = 6
if 3 <= num < 5:
    print('3 to 5')
else:
    print("5 +")

num = 5
if num >= 3 or num == -2:
    print('3 + or -2')

# compare string
name1 = "Ahsan"
name2 = "ahsan"

if name1 == name2:
    print("Same Name")
else:
    print("Name doesn't match")

if name1.lower() == name2.lower():
    print("Same Name by lower method")

# Not equals to
name = "Unknown Person"
if name != "Steve Jobs":
    print(name)


# nexted condition
x = 5
if x < 2:
    print("less than 2")
else:
    if x == 3:
        print("x  is 3")
    else:
        if x == 5:
            print("x is 5")


# iteration

# while loop

'''
while condition:
    statement
'''
x = 1
print(x)
x +=1
print(x)
x +=1
print(x)
x +=1
print(x)
x +=1
print(x)
x = 1
print(x)
x +=1
print(x)
x +=1
print(x)
x +=1
print(x)
x +=1
print(x)



# 5 time repetition
print("While loop")
x = 1
while x <=100:
    print(x)
    x = x + 1

# infinite loop
x = 1
while True:
    print(x)
    x += 1
    if x >10:
        break
# Omit even number 1 to 20
x = 0
while x < 20:
    x +=1
    if x %2 == 0:
        continue
    print(x)

# for loop
'''
for element iterable:
            statement
'''
# sum 1 to 10
sum = 0
for num in range(1, 11):
    print(num)
    sum += num
print("Sum is {sum}".format(sum=sum))
# String characters by for loop
title = "Apple Inc."
for char in title:
    print(char)
#List
cars = ['honda','toyota','audi']
print(cars)
print(cars[0])
print(cars[2])
#Mixed List
mix_list = ['honda',29,4.4, False]
print(mix_list)

#Last element of list
print(mix_list[-1])
#empty list
cars =[]
#print(cars[0]) #Will throw error

#2D List or Matrix
'''
1 2 3 4 5
4 5 6 7 8 
1 1 1 1 1
0 0 0 0 0
'''

#Nested list
matrix = [ [1, 2, 3, 4, 5],
            [4, 5, 6, 7, 8],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
         ]
for x in matrix:
    for y in x:
        print(y,end='')
    print()

#list slicing
numbers_list = [1, 2, 3, 4, 5]
print(numbers_list [0 : 2])
print(numbers_list[2 : -1])

#list iteration by for loop
cars = ['honda','toyota','audi']
for car in cars:
    print(car)
    if (car == 'toyota'):
        print("I love toyota")

# sum of list numbers
list_of_number = [1, 2, 'Math', 4, 5.5, 5]
sum = 0
for num in list_of_number:
    if type(num) == int:
     sum += num
print("Sum is: {sum}".format(sum = sum))

#List modification
mix_list = ['honda', 29, 4.4, False]
print(mix_list)
mix_list[0] = 'toyota'
print(mix_list)

#Adding item in list
mix_list.append('audi')
print(mix_list)

mix_list += ['mercedez'] # shortcut version for adding item
print(mix_list)

mix_list +=['mercedez'] #shortcut version for adding item
print(mix_list)

mix_list.insert(2,'proton')
print(mix_list)

#Deleting item in list
cars = ['honda', 'toyota', 'audi']
del cars [0]
print( cars )

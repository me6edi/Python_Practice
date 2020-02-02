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

#Get and remove item using pop()
cars = ['honda', 'toyota', 'audi']
last_car = cars.pop()#last item
print(cars, "\n",last_car)

cars = ['honda', 'toyota','audi']
second_car = cars.pop(1) #second item
print(cars, "\n", second_car)

#Remove list item by value
numbers = [1,2,3,4,5,6,5]
numbers.remove(5)
print(numbers)#Remove the first value it finds in list
# Splitting Strng into list items
import re
cars = "toyota, honda, bmw, audi"
#cars = ['toyota', 'honda', 'bmw', 'audi']
car_list = re.split(',', cars)
print(car_list)
#List's string item concatnatin
quote = ['love','is', 'blind']
print(quote)
quote_str = ''.join(quote)
print(quote_str)

#Sorting list
# cars = ['toyota','honda','audi','bmw']
# print(cars)
# cars.sort()
# print(cars)
# cars.sort(reverse =True)
# print( cars )

#shorted list
cars = ['toyota', 'honda','audi', 'bmw']
print(sorted(cars))# doesn't affect original list
print(cars)

#REversing list
numbers = [1,2,3,4]
numbers.reverse()
print(numbers)

#list length
numbers = [1,2,3,4]
print(len(numbers))

# checking value exist in list
numbers = [1,2,3,4]
if 2 in numbers:
    print(" 2 is in number")

if 20 not in numbers:
    print("20 does not exist")


# ----------------------
#     tuple
#----------------------

#Syntax
tp = (1,2, 'bill', 4.4, False)
print(tp,type(tp))

#this is not tuple
a = 1,2
print(a)

s= ('hi')
print(s, type(s))

# Access
tp = 1,2, 'bill', 4.4, False
print(tp[0], tp[2], tp[-1], sep='|')

#Iteratin
tp = 1,2,'bill', 4.4, False
for t in tp:
    print(t)
#Comparing
t1 = 1,2,3
t2 = 1,2,3
if t1 == t2:
    print("t1 and t2 values are equal")
# Immutable
# t1 = 1,2,3
# t1[0] = 2

# Unpacking or Multiple assignment
t1 = 5, 7, 11
x, y,_ = t1
print(x,y,z, sep = ' | ')

#--------------------
#     Dictionary
#--------------------
#Syntax
''''
dict = {key : Value}
'''
dict = {} # empty dictionary
dict ['name'] = 'Swift'
dict['age'] = 55
print(dict['name'], ' | ', dict['age'])

#Dictionary len
dict = {'bill' : '01010101','steve' : '04040404'}
print(dict['bill'])
print(dict['steve'])
print(len(dict))

# Modification
shop_items_price_kg = {'rice' : 44 , 'flour' : 33}
print(shop_items_price_kg)

# Adding new item
shop_items_price_kg['0il'] = 39
print(shop_items_price_kg)

#Deleting item
del shop_items_price_kg['0il'] #remove key | value pair
print(shop_items_price_kg)

#Editina item
shop_items_price_kg ['rice'] = 90
print(shop_items_price_kg)

#Iteration
#key and  value
asci_dict ={'a':97, 'b':98, 'c':99, 'd':100}

for key, value in asci_dict.items():
  print(key, value, sep='->')
  print(key)

# Iterate value only
for value in asci_dict.values():
    print(value)
#Sorted keys while iterate
shop_items_price_kg = {
    'rice' : 44,
    'flour': 33,
    'oil': 33
}
print(shop_items_price_kg)
print(shop_items_price_kg)
for key in sorted (shop_items_price_kg):
    print(key,shop_items_price_kg[key])
# Empty set
num_set = set()#{} reserved for dictionary

## Add elements
num_set.add(1)
num_set.add(2)
num_set.add(3)
num_set.add(4)
num_set.add(5)
num_set.add(6)
print(num_set)# nique values 1 i shown oly one time


## Set operations
set_a = {1, 2, 3, 4, 5, 1}
set_b = {6, 5, 4, 7, 8, 8}
print('Set A:', set_a)
print('Set B: ',set_b)

print('A-B',set_a - set_b)# items in set_a but not in set_b

print("A|B", set_a | set_b) # items in set_a or set_b or both
print('A&B', set_a & set_b)# common items in set_a and set_b
print('A^B', set_a ^ set_b) # items in set_a or set_b but not both

# Check item exist or not
set_country = {'bangladesh', 'malaysia', 'singapore','usa'}
country = 'bangladesh'
if country in set_country:
    print(country.title(), 'exists')
#-----------------
#    Function
#-----------------

#Define
#sequence of statements can be defined as function
def welcome():
    print('Hello World')
    for x in range(0,10):
        print('HI',str(x))
welcome()
welcome()

print(len('Hello world'))
print(max(2, 4))

#parameter
def welcome(name): # name is parameter
    print(f"Welcome {name}")

welcome('Bill') # 'Bill' is argumet
welcome('Steve')

# Positional argument
def person_details(name, age, country):
    print(name,age,country, sep=' | ')
person_details('Bill', 55, 'US')
person_details('Swift', 40 , 'Canada')

#keyword argument
def person_dtails(name, age, country):
    print(name, age, country, sep=' | ')

## argument order deesn't matter
person_details(name = 'Bill', age = 55, country='US')
person_details(age = 40, country = 'Canada', name ='Swift')

#Default value
def person_details(name, age, country= 'Bangladesh'):
    print(name, age, country, sep = ' | ')

    person_details(name = 'Bill', age = 55, country ='US')
    person_details(name = 'Swift', age = 40)# default value keyword arg
    person_details('Alam', 30) #default value positionnal org

#Return value
def square (num):
    return num * num

print(square(2), square(2.2), sep = ' | ')


def get_name(first_name, last_name):
    return first_name + "" + last_name

print(get_name('Bill', 'Gates'))
print(get_name('Steve', 'Jobs'))


#Optional argument
def get_name(first_name, last_name, middle_name=''):
    complete_name = first_name
    if middle_name:
        complete_name += '' + middle_name

    complete_name += '' + last_name
    return complete_name


print(get_name('Bill', 'Gates'))
print(get_name('Bill', 'Gates', 's'))

# Function are first-class object
def str_upper(str):
    return str.upper()

print(str_upper("hello"))
stup = str_upper
print(stup("hello"))


#Function are first-class object
def str_upper(str):
    return str.upper()

# Function can be pased as argument
def greetings(func):
    greet = func("Welcome, nice to meet you")
    print(greet)

greetings(str_upper)

#Function are first-Class object
def str_upper(str):
    return str.upper()

#Functional programming
up_list = list(map(str_upper, ["life", "is", "Cool"]))
print(up_list)

#Nested Function
def hello_world(str):
        def print_upper(s):
            return s.upper()

        print(print_upper(str))

hello_world("mango")


## Value Type
num = 100
def change_num(n):
    n+= 100
    print( f"Inner num: {n}")
change_num(num)
print( 'Outside num: ' + str(num))

#Reference Type
# List, Dictionary
num_list = [1, 2, 3, 4, 5]
num_dict = {'one': 1, 'two': 2, 'three': 3}
def change_num_list(list, dict):
    del list[0]
    list[-1] = 50

    del dict ['one']
    dict['three'] = 33
    print("Inner List: ", list)
    print("Inner Dict ", dict)

print("Before")
print("Outer List: ", num_list)
print("Outer Dict: ", num_dict)
change_num_list(list=num_list, dict = num_dict)
print("After")
print("Outer List: ", num_list)
print("Outer Dict: ",num_dict)
#Arbitrary number of arguments
def students(*students_name):
    print(students_name, type(students_name))
    for student in students_name:
        print(student)


students('Bill', 'Steve', 'jonathon', 'Jack', 'Bionic')
students()
students('Jack')

# Positional and Arbitrary arguments mixing
def students(captain, *other_students):
    print('Captain', captain)
    print('Others', other_students)

students('Mahmud', 'Fuad', 'Emon', 'Maruf', 'Arif')

# Arbitrary keyword arguments
def students(captain, **other_students):
    print('Captain', captain)
    print('Others', other_students)

students(captain='Mahmud', second_captain='fuad',third_captain='emon')

## Arbitrary keyword arguments are optional
students(captain='Mahmud')

#----------------------
#     Lambda
#----------------------

## Anonymos or Inline function
add_nubers = lambda x, y: x + y #auto return lambda expression
print(add_nubers(2,3))

# Anonymous or Inline function
bd_public = lambda name: "Bangladeshi Citizen: " + name
print(bd_public('Mehedi'))

#-------------------------
#        Class
#-------------------------
# Global varible
restaurant_name =  '7 Eleven'
restaurant_owner =  'Mehedi'

def restaurant_details():# function
    print(restaurant_name, restaurant_owner)

def another_restaurant():
    #Local variable
    restaurant_address = 'Bogra'
    print(restaurant_name, restaurant_owner)
    print(restaurant_address)

restaurant_details()
another_restaurant()


#class second example
class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def details(self):
        print(self.name, self.age, sep=' | ')


bill1 = Person()
bill1.details()


bill2 = Person('Bill', 55)#self pass automatically
bill2.details()

## Third example
people_list = []
for x in range(0,3):
    person = Person("Person"+str(x), 30+x)
    people_list += [person]

for x in people_list:
    x.details()

#class variable and Instance variable Details
class Alien:
    legs = 5 # class variable

    def __init__(self,name):
        self.name = name #instance variable


##Instantiation
alien1 = Alien('Maven')
alien2 = Alien('Woven')

print(alien1.name, alien2.name)#accessing instance variable
print(alien1.legs, alien2.legs)#accesssing class variable

Alien.legs = 10
print(alien1.legs, alien2.legs)

alien1.__class__.legs = 99
print(alien1.legs, alien2.legs)

# Attribute value modification

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def change_name(self, name):
        self.name = name
    def details(self):
        print(self.name, self.age, sep= ' | ')

#Directly change
person_x = Person(name='Stone Cold', age=49)
person_x.details()


person_x.name = "Rock"
person_x.details()

# Indirectly change by instance's method
person_x.change_name('Triple X')
person_x.details()

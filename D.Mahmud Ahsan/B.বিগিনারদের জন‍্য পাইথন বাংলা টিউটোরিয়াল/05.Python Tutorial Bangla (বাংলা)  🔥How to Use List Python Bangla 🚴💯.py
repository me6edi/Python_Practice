#list


cars = ['hondsa', 'toyota', 'audi']
print(cars)
print(cars[0])

#mixed list
mix_list = ['honda', 29, 4.4, False, 'audi']
print(mix_list)
#Last eliment of list
print(mix_list[-1])

# 2D List or matrix
''''
1 2 3 4 5
4 5 6 7 8
1 1 1 1 1
0 0 0 0 0
'''
#Nested List
matrix = [
    [1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

for x in matrix:
    for y in x:
        print(y, end=' ')
    print()

# list slicing
numbers_list = [1, 2, 3, 4, 5]
print(numbers_list[2:-2])

#list iteration by for loop
cars = ['honda', 'toyota', 'audi']
for car in cars:
    print(car)

# sum of list numbers
list_of_number = [1, 2, 'Math', 4, 5, 5.5, 5]

sum = 0
for num in list_of_number:
    if type(num) == int:
        sum += num
print("Sum is: {sum}".format(sum=sum))

# List modification
mix_list = ['honda', 29, 4.4, False]
print(mix_list)

# add item
mix_list.append('audi')
print(mix_list)

mix_list += ['bmw']
print(mix_list)

mix_list.insert(2, 'proton')
# Deleting item in list
del mix_list[0:3]
print(mix_list)

#Get and remove item using pop()
cars = ['honda', 'toyota', 'audi']
last_car = cars.pop()
print(cars, '\n',last_car)

# Remove list item by value
numbers = [1, 2, 3, 4, 5, 6, 5]
print(numbers)
numbers.remove(5)
print(numbers)

# Splitting String into list items
import re
cars = "toyota , honda, bmw, audi"
car_list = re.split(',', cars)
print(car_list)

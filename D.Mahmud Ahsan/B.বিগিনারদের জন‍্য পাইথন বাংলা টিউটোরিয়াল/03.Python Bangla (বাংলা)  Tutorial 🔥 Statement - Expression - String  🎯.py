# Stacement
print("Hello world")

# Expression
x = 10
y = x + 2
print(x,y)

# String
title = "Pyhon Course"
print(title[0], title[1], title[2], title[-1], title[-2])

# String Operation
name = 'Mehedi Amin'
print(name.title())
print(name.upper())
print(name.lower())
print(name.upper().lower().title())
#String Concatenation
first_name = "Steve"
last_name = "Jobs"

name = first_name +'\n'+ last_name
print(name)

name = "       Mr. X    "
print('_' + name + '_')
print('_' + name.lstrip()+ '_')

# Printing Single and Double Quote
shop_name = "Rahim's Shop"
print(shop_name)
shop_name = 'Rahim" Shop'
print(shop_name)

shop_name = 'Rahim\'s Shop'
print(shop_name)

# Find word in sentence
sentence = "A quick brown fox jumps over the lazy dog"
print(sentence.find('fox'))
print(sentence.find('foxs'))

#Replace text
sentence  = 'A quick brown fox jumps over the lazy dog'
sentence = sentence.replace('fox','tiger')
print(sentence)

sentence = "A quick brown fox jumps over the lazy fox"
sentence = sentence.replace('fox', 'tiger')
print(sentence)

#Print separator ice
x = 'Dhaka'
y = 'Bogra'
z = 'Comilla'
a = 300
b = 200
c = 400

print('Dhaka','|','Bogra','|','comilla')
print('300','|','200','|','400')
print(x,y,z, sep=' | ')
person = "Mr.x's age is 77"
print(person)

person = "{name}'s age is {age}"
print(person.format(name='Mehedi Amin', age = 20))

person = '%s\'s age is %d'
print(person % ('Bil', 55))

name = "Taylor Swift"
part_of_name = name[7:-1]
print(part_of_name)

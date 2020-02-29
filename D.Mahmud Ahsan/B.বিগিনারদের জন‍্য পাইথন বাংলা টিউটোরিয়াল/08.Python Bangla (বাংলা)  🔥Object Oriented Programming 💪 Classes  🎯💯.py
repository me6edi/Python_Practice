# ---------------------------------------------
#         Class
# ---------------------------------------------

# Syntax

''''
class className (ParentClass):
    variables
    methods
'''


# Global varible

# class Restaurant:
#     name = ' '
#     owner = ' '
#
#
restaurant_name = 'Doi ghor'
restaurant_owner = 'Mehedi'


def restaurant_details():
    print (restaurant_name, restaurant_owner)


def another_restaurant():
    # Local variable
    retaurant_address = 'bogura'
    print(restaurant_name, restaurant_owner)
    print (retaurant_address)


restaurant_details()
another_restaurant()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print (self.name, self.age, sep=' | ')

people_bill = Person('Bill', 55)
for x in range(0,3):
    person = person("Person" + str(x), 30+x)
    person_list += [person]
bill.details()
print (bill.name, bill.age)

for x in people_list:
    x.details()

class X:
    def __init__(self, name):
        self.name = name
        print(self.name + " created")
    def __del__(self):
        print (self.name + " is destorayed")



x = x('x')
y = x('y')
print ("Hello world")



def hello():
    x = X('hello_X')
    y = X('hello_Y')


# Inheritence

class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self):
        return self.X + self.y


math_obj = Math(2,4)
print (math_obj.sum())

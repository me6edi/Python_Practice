#------------------------------------------
#          Function
#----------------------------------------

#Define

def welcome():
    print('Hello world')
    for x in range(0,10):
        print("HI", str(x))





welcome()
welcome()
welcome()

#parameter
def welcome (name):
    print("Welcome {name}".format(name=name))

welcome('Bill')
welcome('Steve')

#Keyword argument
# def person_details(name, age, country):
#     print(name, age, country, sep=' | ')
#
# # argument order doesn't matter
# person_details(name="Bill", age=55, country='US')
# person_details(name='Swift', age=40, country='Canada')

# DEfault value
def person_details(name, age, country ="Bangladesh"):
    print(name, age, country, sep=' | ')

person_details(name='Bill' , age=55, country='US')
person_details(name='Swift', age=40)
person_details('Alam', 30)
#Return Value

def get_name(firs_name, last_name):
    return firs_name + "" + last_name
print(get_name('Bill', 'Gates'))
print(get_name('Steve', 'Jobs'))

#optional argument
def get_name(firs_name, last_name, middle_name=''):
    complete_name = firs_name
    if middle_name:
        complete_name += ' ' + middle_name
    complete_name += '' + last_name
    return complete_name


print(get_name('Bill', 'Gates'))
print(get_name('Bill', 'Gates', 's'))

## Value Type
num = 100
def change_num(num):
    num +=100
    print("Inner Num: {num}".format(num=num))

change_num(num)
print('Outside num: ' + str(num))
#list Dictionary
num_list = [1, 2, 3, 4, 5]
num_dict = {"one": 1,'two': 2, 'tharee':3}

def change_num_list(list,dict):
    del list[0]
    list[-1] = 50

    del dict['one']
    dict['three'] = 33
    print("Inner List: ",list)
    print("Inner Dict: ", dict)
print('Before')
print("Outer list: ", num_list)
print("Outer Dict: ", num_dict)
change_num_list(list=num_list, dict=num_dict)
print("After")
print("Outer List: ", num_list)
print("Outer Dist: ", num_dict)

# Arbitrary number of arguments
def students(*students_name):
    print(students_name, type(students_name))
    for student in students_name:
        print(student)

students('Bill', 'Steve', 'Jonathon', 'jack', 'Bionic')
students()
students('Jack')

## Positonal and Arbitrary arguments mixig
def students(Captain, *other_students):
    print('Captain ', Captain)
    print('Others ', other_students)

students('Mahmud', 'Fuad', 'Emon', 'Maruf', 'Arif')
# students(captain='Mahmud', second_captain='fuad', third_captain='emon')

add_numbers = lambda x , y: x + y

print(add_numbers(2,3))

bd_public = lambda name:'Bangladeshi Citizen' + name
print(bd_public(' Mehedi'))

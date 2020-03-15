#------------------------
#      Generator
#------------------------

#Iterable
str = "Hello World"
for i in str:
    print(i)

# List Comprehension
list = [x*x+2 for x in range(1, 5)]
for item in list:
    print(item)

# Generator
gen = (x*x+2 for x in range(1, 5)) # Generator comprehension
for item in gen:
    print(item)

#xargs



def student(*detils):
    print(detils[0])


student(101,"Mehedi",4.5)
student(102,"Mehedi Amin",3.5)

def add(num1,num2):
    sum = num1 + num2
    print(sum)

add(20,50)

def addnum(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
addnum(50,100)

#xxargs

def student(**details):
    print(details)

student(id = 101,name = "Mehdi Amin")
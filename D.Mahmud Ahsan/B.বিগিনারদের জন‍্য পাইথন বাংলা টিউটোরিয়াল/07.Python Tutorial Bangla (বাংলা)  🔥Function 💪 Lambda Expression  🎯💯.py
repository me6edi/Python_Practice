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

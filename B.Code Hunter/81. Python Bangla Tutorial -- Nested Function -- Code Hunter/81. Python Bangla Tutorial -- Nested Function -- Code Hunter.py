#nested function
a =5
def f():
    #a = 5#nonlocal
    def g():
        #a = 6
        return a*a
    print('a * a = ',g())

f()

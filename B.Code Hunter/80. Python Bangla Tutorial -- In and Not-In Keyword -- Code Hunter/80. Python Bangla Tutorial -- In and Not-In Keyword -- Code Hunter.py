#dested function
a = 5
def f():
    def g():
        a = 6
        return a*a
    print(a,'a * a = ',g())

f()

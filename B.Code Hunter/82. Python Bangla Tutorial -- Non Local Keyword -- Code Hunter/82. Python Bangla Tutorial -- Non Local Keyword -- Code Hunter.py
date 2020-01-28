#nonlocal
x = 6#global
def f():
    x = 5#nonlocal = not global and local
    def g():
        nonlocal x
        x = 8

    g()
    print('x = ', x)


# x = 8  #local
f()


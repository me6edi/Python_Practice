# None keyword
i = None


def func(a):  # a = 10
    if a is None:
        return 'There is no value.'
    else:
        return a * 2


print(func(10))
print(func(i))

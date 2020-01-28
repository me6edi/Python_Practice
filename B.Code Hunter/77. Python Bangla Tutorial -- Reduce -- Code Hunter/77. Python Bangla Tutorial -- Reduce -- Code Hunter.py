# reduce
# reduction -> reduce
# reduce = binary>function,swquence
from functools import reduce

# def func(x, y):
#     return x * y
#
# a = [1, 2, 3, 4, 5]

b = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6])

print(b)

# comprehension and conditional
# a = {x | x E N and x is even number and 1<=x<=10
# expresion,range/enumerate,conditon
a = [x ** 2 + x for x in range(1, 11) if x % 2 == 0]
print(a)

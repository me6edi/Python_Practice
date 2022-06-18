# object comparison '==' VS 'is'
x = [1, 2, 3]
xx = x

print(x == xx)
print (x is xx)

y = list(x)
print(x == y)
print(x is y)

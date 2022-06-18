# List concateante
p = [1, 2, 3]  # list
q = [4,5,6]
r = 10  # a number
print(p + q)

matrix = [
    [1,2,3,4,],
    [5,6,7,8],
    [22,33,44,5],
    [34,44,55,22]
]
for x in matrix:
    for y in x:
        print(y, end=' ')
    print()

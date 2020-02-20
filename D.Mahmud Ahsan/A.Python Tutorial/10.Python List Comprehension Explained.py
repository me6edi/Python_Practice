#----------------------------------
#   Comprehesnion Syntax
#----------------------------------
""""
It is produced one series of values based on processing of another series
Syntax list
[expression for value in iterable if condition]
"""


## List comprehension
num_squares = [v * v for v in range (1, 11)]
print(num_squares)

# print()
## normal way
num_squares = []
for v in range(1, 11):
    num_squares += [v * v]

print(num_squares)

## List comrehension
## odd num only
num_squares = [v * v for v in range(1, 11) if v%2 !=0]
print(num_squares)

## Dictionary expression
num_dict_sq = {v*v for v in range (1, 11) if v%2  !=0 }

print(num_dict_sq)

## Set expression
num_set_sq = {v * v for v in range(1, 11) if v%2 != 0}
print(num_set_sq)

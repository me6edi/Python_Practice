#-----------------------------------------
#       Script arguments
#-----------------------------------------
# import sys
# from mspack import msmath
#
# def process_command(*args):
#     command = args[0]
#     x       = int(args[1])
#     y       = int(args[2])
#
#     if command == 'sum':
#     print('Sum is: ',
#     msmath.sum(x, y))
#     if command == 'sub':
#         print("Subtraction is:", msmath.subtract(x,y))
#     if command == 'mul':
#         print('Multiplication is: ')
#     if command == 'div':
#         print('Divison is: ')
#
#
# if len (sys.argv) >=4:
#     # valid commands: sum sub mul div
#     command = sys.argv[1].lower()
#     x       = sys.argv[2]
#     y       = sys.argv[3]
#
#     try:
#         process_command(command, x, y)
#     except Exception as e:
#         print("Error in process_coommand: ", e)
#
# else:
#     print("Command and Paramters are not sufficient")
#
# ## Empty set
# mum_set = set()
# mum_set.add()

# Set operations
# set_a = {1, 2, 3, 4, 5, 1}
# set_b = {6, 5, 4, 7, 8, 8}
# print("Set A: ", set_a)
# print("Set B: ", set_b)
#
# print("A-B" , set_a - set_b)
# print("A|B", set_a | set_b)
# print("A&B",set_a & set_b)
# print("A^B", set_a ^ set_b)

## Check item exist or not
set_country = {'bangladesh', 'malsysia', 'singapore', 'usa'}
country = 'bansgladesh'

if country not in set_country:
    print(country.title(), 'exists')

sum = 100
num = 10
sum += num if num % 2 == 0 else 0
print(sum)

#expression for value in iterable if condition
num_squares = [v * v for v in range(1, 11)]
print(num_squares)

### normal way
num_squares = []
for v in range (1, 11):
    num_squares +=[v * v]
    print(num_squares)


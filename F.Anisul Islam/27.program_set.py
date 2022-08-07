from stat import S_ENFMT


num1 = {1,2,3,4,5,5}
num2 = set([4,5,6])
num2.add(8)
print(num1 | num2)
print(num1 & num2)
print(num1 - num2)
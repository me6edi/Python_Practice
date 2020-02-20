 # single line comment
#Comments

""""
Multiline Comments
"""
''''
Multiline Comments
'''


# Variables

name = "Grocey List"
detail = "Buy from supershop"
number_of_items = 5
budget = 2500 #taka
amount_of_rice = 1.5 #kg
should_we_buy_today = True

print(name, type(name))
print(detail, type(detail))
print(number_of_items,type(number_of_items))
print(budget,type(budget))
print(amount_of_rice,type(amount_of_rice))
print(should_we_buy_today,type(should_we_buy_today))


# camel case
amount_of_rice = 3.33
#snake case
aamount_of_rice = 22


#duck type
age = 5
print(age)
age = 5.5
print(age)
age = "string"
print(age)

# Operators

number_of_items = 5
print(number_of_items)

number_of_items = number_of_items + 2
print(number_of_items)

x = 10
y = 3
result = x / y
print(result)
result = x % y
print(result)

x = 10
x = -x
print(x)
print(abs(x))
result = divmod(x,y)
print(result)

x = 2
result = x ** 4
print(result)


x = 2
result = pow (x,4)
print(result)

# #Innner if statement

# if 7 > 3:
#     if 7 > 3:
#         print("Hi")

# num1 = 30
# num2 = -80
# num3 = -40

# if num1 > num2: # 30 > 20
#     if num1 > num3: # 30 > 40
#         print(num1)
#     else:
#         print(num3)

# if num2 > num1: # 20 > 30
#     if num2 > num3: # 20 > 40 
#         print(num2)
#     else:
#         print(num3)




# value1 = 60
# value2 = 70

# """ 
# if value1 > value2: # 20 > 30
#     print(value1)
# else:
#     print(value2)

# """

# max = value1 if value1 > value2 else value2

# print(max)
 

numbers1 = 20
numbers2 = 30
numbers3 = 40

if numbers1 > numbers2 and numbers1 > numbers3:
    print(numbers1)
elif numbers2 > numbers1 and numbers2 > numbers3:
    print(numbers2)
else:
    print(numbers3)

#Vowel - a,e,i,o,u
ch = 'w'

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print("Consonent")
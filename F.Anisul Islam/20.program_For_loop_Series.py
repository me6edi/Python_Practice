# 1 + 2 + 3 + ..... + n
# n = int(input("Enter theh last number: "))
# sum = 0

# for x in range(1,n+1,1):
#     sum = sum + x

# print(sum)

# 2 + 4 + 6 + ..... + n
# n = int(input("Enter theh last number: "))
# sum = 0

# for x in range(4,n+1,4):
#     sum = sum + x
#     print(x)

# print(sum)

# n = int(input("Enter theh last number: "))
# sum = 0

# for x in range(1,n+1,1):
#     sum = sum + x*x
#     print(x)

# print(sum)


n = int(input("Enter theh last number: "))
sum = 1

for x in range(1,n+1,1):
    sum = sum * x*x
    print(x)

print(sum)
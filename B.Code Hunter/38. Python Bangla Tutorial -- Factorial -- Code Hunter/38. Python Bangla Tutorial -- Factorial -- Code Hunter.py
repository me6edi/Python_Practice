#factorial
#1*2*3....*n
n = int(input("Enter a number: "))
fact = 1

while n >=1:
    fact = fact * n
    n = n - 1

print(fact)

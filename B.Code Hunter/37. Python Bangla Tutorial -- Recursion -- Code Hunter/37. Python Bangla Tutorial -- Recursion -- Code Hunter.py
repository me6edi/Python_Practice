#recursion
#factorial(n) = 1*2*3*...*n
#factorial(1) = 1
#factorial(n) = n*factorial(n-1) = n

def factorail (n):
    if n == 1:
        return 1
    else:
        return n * factorail(n-1)
print("Enter Your number: ")
n = int(input())
print("Recursive Value is: ",factorail(n))

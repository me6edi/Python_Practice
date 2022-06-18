def print_greatest_no(a, b, c):
    greatest = 0
    if a > b:
        if a > c:
            greatest = a
        else:
            greatest = c
    elif b > a:
        if b > c:
            greatest = b
        else:
            greatest = c
    else:
        greatest = c
    print(greatest,"is greatest")


a = 40
b = 20
c = 30

print_greatest_no(a, b, c)

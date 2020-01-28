#continue statement

p = [1,2,3,12,4,5,6,7]

def continu(list):
    for i in list:
        if i < 10:
            continue
        return i


print(continu(p))

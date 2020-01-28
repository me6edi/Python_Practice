def add(p, q, r):
    return p + q + r


def add1(q, p, r):
    return p - q + r


# forwarding function
def add2(p, q, r):
    return add1(p,q,r)


d1 = [1000, 20, 10]
s = add(*d1)
print(s)

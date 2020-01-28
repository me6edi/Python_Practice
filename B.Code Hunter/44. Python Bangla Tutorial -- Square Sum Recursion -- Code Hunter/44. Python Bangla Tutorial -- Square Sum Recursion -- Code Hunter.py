#square sum - recurtion
#1^2+2^2+3^2+......+n^2
#1*1+2*2+3*3+4*4.....(n-1)


def sqr_sum(n):
    if n == 1:
        return 1
    else:
        return n*n + sqr_sum(n-1)


a = int(input()) #3*3=9 + 2*2=4 + 1*1 =1
b = sqr_sum(a)
print(b)

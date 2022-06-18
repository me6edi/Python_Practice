#permutastion using compreshension
#(a,b) (a,b) = {(a,a),(a,b),(b,a),(b,b)}

a = ['a','b']
b = [2,3]
s = [(x,y) for x in a for y in b]
print(s)

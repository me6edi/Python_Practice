#bubble short

p = [8,2,4,1]

print("Before Shorting: ",p)
i = 0
while i < len(p):
    j = 0
    while j < i:
        if p[i] < p[j]:
            #swap
            temp = p[i]
            p[i] = p[j]
            p[j] = temp
        j = j + 1

    i = i + 1

print("After shorting: ",p)



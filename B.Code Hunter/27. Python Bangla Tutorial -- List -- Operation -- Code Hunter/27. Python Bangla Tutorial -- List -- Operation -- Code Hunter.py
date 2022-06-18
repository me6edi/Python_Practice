#list in operastion
p = ["apple","orange","bannana","Pineaple"]
p.append("drink")
p.remove("bannana")
del p[1]
print("orange" in p)

if "apple" in p:
    print("TRUE")
else:
    print("FALSE")

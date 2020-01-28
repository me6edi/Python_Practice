#Grade & Grade point
print("Enter you marks:")
mark = int (input())

if mark > 80: #Mark = 80 ->100
    if mark < 100:
        print("A+")

elif mark > 75:
    if mark < 79:
        print('A')

elif mark > 70: #Mark = 70 - 74
    if mark < 79:
        print('A-')

elif mark > 65: #Mark = 65 - 69
    if mark < 69:
        print('B+')

elif mark > 60: #Mark = 75 - 79
    if mark < 64:
        print('B')

elif mark > 55: #Mark = 55 - 59
    if mark < 59:
        print('B-')

elif mark > 50: #Mark = 50 - 54
    if mark < 54:
        print('C+')

elif mark > 40: #Mark = 40 - 49
    if mark < 49:
        print('C')

elif mark > 40: #Mark = 40 - 44
    if mark < 44:
        print('D')

else:
    print("Fail") #Mark = 00 - 39

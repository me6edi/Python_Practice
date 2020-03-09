#-----------------------------
#     Regular Expression
#-----------------------------

## Text pattern matching
import re
date_data = '13/Feb/2019 I will go Canada'

if re.match(r'\d+/[a-zA-Z]+/\d{4}', date_data):
    print("Matched")
else:
    print("Mismatched")

date_data = '13/Febb/2019 I will go Cana da'
date_pattern = re.compile(r'\d+/[a-zA-Z]+/\d{4}')

if date_pattern.match(date_data):
    print("Matched")
else:
    print("Mismatched")

text = "I am Good , but I am Not very good"
list = re.findall('good', text, flags =re.IGNORECASE)
print(list)
text = re.sub('g00d', 'bad', text, flags=re.IGNORECASE)
print(text)

num = re.compile(r'\d+')
list = num.findall('12345')
print(list)

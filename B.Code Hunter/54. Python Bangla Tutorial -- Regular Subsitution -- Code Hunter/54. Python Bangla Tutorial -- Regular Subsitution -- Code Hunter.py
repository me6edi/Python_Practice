#regular expresion - substitution
import re
#re.sub(pattern,replacement,string)
a = 'This is 1234 to 4567 haha'

#/d means digit
#/D means nonedigit

p = re.sub('\D','0',a)
print(p)


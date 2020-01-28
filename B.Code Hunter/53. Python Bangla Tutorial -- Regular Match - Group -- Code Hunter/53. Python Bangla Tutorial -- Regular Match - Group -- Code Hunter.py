#regular expresion - match

import re

a = "My name is Mehedi and he is a student"

#re.match(pattern,string,falgs(optional))


p = re.match('(My.*)(and) (.*student)',a,re.I)

if p:
    print('Match')
    print('Group-1: ',p.group(1))
    print('Group-2: ',p.group(2))
    print('Group-3: ',p.group(3))
else:
    print('Not Match')


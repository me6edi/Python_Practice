#word subtitutde

import re

a = 'This is a number 1234 5678'
#re.sub(pattern,replacement,string)
#\w = word charecter
b = re.sub('\w+','Mehedi',a)

print(b)

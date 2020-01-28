#searching - gmail
import re

a = 'me6edi@gmail.com'
#re.search(pattern,string,flags<optional>)
#\w = word charecter
# + = one or more
# * = Zero or more
# . = any charecter
b = re.search('\w+\.*\w+@\w+\.\w+',a)

if b:
    print("Found")
else:
    print("Not Found")

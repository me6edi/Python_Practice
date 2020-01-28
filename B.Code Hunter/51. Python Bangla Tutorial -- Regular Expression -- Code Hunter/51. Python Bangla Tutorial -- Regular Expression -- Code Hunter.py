# regular expresion
import re # r = regular and e = expresion

a = 'My name is Mehedi and i am a student'
#re.search(pattern,string,flags<optional>)
# (.*---.*)
#.means match any charecter
#* means zeroor more
#Flags <optional>
#re.I means case insensitive

p = re.search('.*is.*',a,re.I)

if p:
    print('Found')
else:
    print('Not found')

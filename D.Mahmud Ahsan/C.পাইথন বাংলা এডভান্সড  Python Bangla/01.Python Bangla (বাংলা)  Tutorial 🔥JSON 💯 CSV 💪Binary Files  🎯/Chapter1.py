#---------------------------
#        Files
#---------------------------


## Reading full contents of a text file
"""
Encouraged way with keyword close the file automatically
"""
try:
	with open('data/article.txt') as fobj:
		contents = fobj.read()
		print(contents)
except Exception as e:
	print("File Error: ", e)

### Reading line by line and make uppercase
with open('data/article.txt') as fobj:
	for num, line in enumerate(fobj):
		print(num+1 , line.upper())

### Reading list of line
# with open ("data/names.txt") as fobj:
# 	lines = fobj.readlines()
# print(lines)

''''
w = write # erase existing content if any
a = append
r = read # default
OR
wt =write
at = append
rt = read
t is for test mode shich is set by default
'''


#open and read the file after the appending:
f = open("data/article.txt", "r")
print(f.read())


f = open ('example.txt', 'w')
f.write('I am Writing \n')
f.close()

f = open ('example.txt', 'r')
print(f.read())
f.close()
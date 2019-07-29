file = open('ex.txt','r')
file.seek(0)
file.close()
content = file.readlines()
print (content)
content = [i.rstrip('\n') for i in content]
print (content) 
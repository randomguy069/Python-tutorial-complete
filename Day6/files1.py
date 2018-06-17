fil = open("example.txt",'r')
fil.seek(0) #Will place pointer back at 0 point
content = fil.readlines()
print(type(content))
print(content)
fil.seek(0) #Will place pointer back at 0 point
#Research about seek method
content = [i.rstrip("\n") for i in content] #Used to remove \n
print (content)
fil.close()

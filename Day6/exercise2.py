fi = open("fruits.txt",'r')

content = fi.readlines()
con =[i.rstrip("\n") for i in content]
for i in con:
    print (len(i))
fi.close()

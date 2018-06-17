#to write
#fo = open("example1.txt",'w')
#fo.write("\nEric Cartman is a king")

#t
fo =open("example1.txt",'w+') #Used to append
fo.write("Kenny dies in every episode")
fo.write("\nEric Cartman is a king")
fo1=open("example1.txt",'r')
fo.seek(0)
con=fo1.readlines()
print(con)
fo.close()

#read about all these
#r
#r+
#w
#w+
#a
#a+

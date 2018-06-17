import datetime
filename = datetime.datetime.now()
fil1 = open(filename.strftime("%Y-%m-%d-%H-%M-%S")+".txt","w+")
fil2 = open("file1.txt",'r');
fil3 = open("file2.txt",'r');
fil4 = open("file3.txt",'r');
con2 = fil2.read()
con3 = fil3.read()
con4 = fil4.read()
fil1.write(con2+"\n")
fil1.write(con3+"\n")
fil1.write(con4+"\n")

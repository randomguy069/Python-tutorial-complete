numbers = [1,2,3]
fi = open("example2.txt","w+")

for i in numbers:
    fi.write(str(i))
    fi.write("\n")

fi.close()

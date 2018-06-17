with open("example1.txt","a+") as file:
    file.seek(0)
    content = file.read()
    file.write("\nGlory Glory Man United")

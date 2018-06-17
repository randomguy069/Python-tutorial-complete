def cel_to_fahr(temp):
    fahr = (float(temp) * 9/5 ) +32
    return fahr

temperatures = [10,-20,-289,100]

fi = open("example3.txt",'w+')
fi.seek(0)
for t in temperatures:
    if t > -273.15:
        fi.write(str(cel_to_fahr(t))+ "\n")


fi.close()

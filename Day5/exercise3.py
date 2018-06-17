def cel_to_fahr(temp):
    if temp < -273.15:
        return "The temperature's fahr cannot be calculated! "
    else:
        f = (float (temp) * 9/5) + 32
        return f

tempList = [10,-20,-289,100]
for temp in tempList:
    print(cel_to_fahr(temp))

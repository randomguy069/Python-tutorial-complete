def cel_to_fahr(cel):
    if int(cel) < -273.15 :
        return "Can't calculate temperature"
    else:
        fahr = (float(cel)*(9/5)) +32
        return fahr

print (cel_to_fahr(32))
print(cel_to_fahr(-274))

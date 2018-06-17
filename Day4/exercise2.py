def retLength(strin):
    if type(strin) == int:
        return "Invalid type"
    elif type(strin) == float:
        return "Another ivalid type"
    else:
        return len(strin)


print(retLength("Adithya"))
print(retLength(10))
print(retLength(10.0))

planet = input("What planet are you from? ")
print(planet)

def currency_converter(rate,euros):
    dollars = euros * rate
    return dollars

euro = float (input("Enter Euros amount"))
rat = float (input("Enter rate"))

print(currency_converter(rat,euro))

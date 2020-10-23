#deconstructuring is taking a tuple and making many variables from it

#here is a tuple
currencies = 0.8, 1.2
#variables for the tuple
usd, eur= c urrencies

#4 tuples

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]

#assigns name and age to items in tuple
for name, age in friends: 
    print(f"{name} is {age} years old")
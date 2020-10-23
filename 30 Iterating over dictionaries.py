#iterating over a dictionary 
friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name, age in friend_ages.items(): #uses the items method to get the values in the dict
    print(f"{name} is {age} years old")

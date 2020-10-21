#you can stores keys and values in dictonaries.  you use curly braces 
# with a dictionary
#dictionaries keep order in which keys were added
#dictionaries use {key:value}
friend_ages = {"Rolf" : 24, "Admm" : 30, "Anne" : 27}
#to return result
print(friend_ages["Rolf"])

#adding an item to a dictionary or changing an existing value.  Keys are obviously unique
#dictionary[key]=value
friend_ages["Bob"] = 70
print(friend_ages)

#a tuple of dictionaries
#use open parens for tupple - curly brackets for dictionary
friends = ( 
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)
#to get a friends name, in this case fiend #0's name
print(friends[0]["name"])
#get the age for Anne
print(friends[2]["age"])
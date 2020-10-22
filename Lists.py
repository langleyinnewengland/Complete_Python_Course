#sqaure brackets are used for a list. 
#generally, the data inside a list should be homongenous - of the same type

#print the friends list
friends = ["Rolf", "Bob", "Anne"]
print(f"my friends are {friends}.")

#format the above nicely. This joins the items in friends with a comma
comma_seperated = ", ".join(friends)
print(f"my friends are {comma_seperated}.")

print(friends[0])
print(friends[1])
#get length of list
print(len(friends))
#multiple lists in a list
friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]
print(friends[0][0])
#its a good idea to annotate log lists like this
friends = [
    ["Rolf", 24], 
    ["Bob", 30], 
    ["Anne", 27],
]

#to add items to a list use the append method.  Append means adding at the end. 
#as such append applies to lists, but not sets
friends.append("Julie")
#remove from a list use the remove method
friends.remove("Julie")
#in a list of lists you must use the entire sublist to remove


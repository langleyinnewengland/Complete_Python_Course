#sets
#sets do not hold order.  Sets use curly braces {}
#Square brackets for a list. Parens for a tuple. Curly brackets for a set
#create a set
#sets can be used to compare one set to another. Thats the set use case
art_freinds = {"Rolf", "Anne"}
science_friends = {"Jen", "Charles"}
#adding to a set
art_freinds.add("Jen")
#sets dont contain duplicates.  Adding an item that already exists wont do anything

art_freinds = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_freinds.difference(science_friends)
print(art_but_not_science)
science_but_not_art = science_friends.difference(art_freinds)
print(science_but_not_art)

#not in both sets use symetric_difference method
not_in_both = art_freinds.symmetric_difference(science_friends)
print(not_in_both)

#members who are in both use the intersection method
art_and_science = art_freinds.intersection(science_friends)
print(art_and_science)

#all people in both groups w/o duplicates use the .union method
all_friends=art_freinds.union(science_friends)
print(all_friends)

#ask the user for a name.  Print out the examples that are in both sets

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

input_friend=input("enter the name of a friend")
user_friends.add(input_friend)
in_both=nearby_people.intersection(user_friends)
print(in_both)
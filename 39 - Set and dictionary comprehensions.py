friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.capitalize() for name in friends_lower & guests_lower}

#gets the friends in both lists
print(present_friends)

# Transforming data for easier consumption and processing is a very common task.
# Working with homogeneous data is really nice, but often you can't (e.g. when working with user input!).

# -- Dictionary comprehension --
# Works just like set comprehension, but you need to do key-value pairs.

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i] #assigns the friends to when they were last seen
    #create a new variable 'i' .  it goes from 0 (start of range function to the length 
    # of the friends list)
    for i in range(len(friends))
    if time_since_seen[i] > 5
}
#prints the firends who were last seen more than 5 years ago
print(long_timers)

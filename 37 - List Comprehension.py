#double the numbers in the list
numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)

#this does the same thing as above
numbers = [0, 1, 2, 3, 4]
doubled_numbers = [number *2 for number in numbers]
print(doubled_numbers)

numbers = [0, 1, 2, 3, 4]  # list(range(5)) is better
doubled_numbers = [num * 2 for num in numbers]
# [num * 2 for num in range(5)] would be even better.

#print the list in lowercase
names = ["Rolf", "Bob", "Jen"]
lower =[name.lower() for name in names] #.lower() method puts case to lower
print(lower)

#check to see if the user entry matches what is in the list.  But convert user entry and list in memory to 
#the same case (lower)

friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"I know {friend}!")
    #use the title method to print friend in title case
    print(f"I know {friend.title()}!")
    

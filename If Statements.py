#check to see if the user entry matches the variable in friend
friend="Rolf"
user_name=input("Enter your Name: ")

#checks to see if friend is Rolf.  The leading identation is needed in the if statement
if user_name == friend:
    print("Hello, friend!")
else:
    print("You aint my friiend")

#check to see if the user entered something

name = input("Enter your name: ")

if name: #this line checks that name is true (meaning does name <> 0))
    print("we know your name.")
else:
    print("What the fuck?")

#this line always prints.  It converts <name> to boolean.  If its true,
#it returns true, false otherwise
print(bool(name)) 



#Friends, Family, or Unknown
friends = ["Rolf", "Bob", "Peter"]
family = ["Mom", "Brit"]

user_name=input("Enter your name: ")

if user_name in friends: #use the in keyword to see if something is in a list
    print("Hello, friend!")
#use elif for multiple layers (otherwise).  As many elif statements can be added as needed
#evealuated in order
elif user_name in family:
    print("hello, family!")
else:
    print("Who the fuck are you?")


# while loops run for an undefined amount of times
# for loops run for a defined number of times
# #this will run forever, until the string is empty
is_learning = True

while is_learning:
    print("You are learning")
    user_input = input("are you still learning?")
    #if user_input is yes, keep loop going.  Otherwisde stop
    is_learning = user_input == 'yes'

user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We're running!")
    user_input = input ("Do you wish to run the program? (yes/no): ")

print("We stopped running")


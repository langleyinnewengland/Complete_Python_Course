#This will print each friend

friends = ["Rolf", "Jen", "Anne"]
#format is 'for [variable] in [list]
for friend in friends: #the variable friend will be assignd to the items in the list in order
    print(friend)

#print the numbers in elements
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for element in elements:
    print(element)

#prints 'hello, world x10

for _ in elements: #the uderscroe is the variable.  Its an underscroe becasue
    #the variable isn't used for anything
    print("Hello, World")


#the range function does the same thing.  This prints the words x10

for index in range(10): #range(10) iterates throught the list 10 times
    print("Hello, World")

#print the numbers 7, 8, 9
for index in range (7, 10):
    print(index)

#to print the numbers 1-100, but every 5th number (1, 6, 11, 16....)
for index in range (1, 100, 5):
    print(index)

#student grades

#create a dictionary and return the name of the students

students = [
    {"name": "Rolf", "grade" : 90},
    {"name": "Bob", "grade" : 78},
    {"name": "Jen", "grade" : 100},
]

for student in students:
    name = student["name"] #gets the name value (key) from the students dictionary
    print (name)

#now return the students and grades
students = [
    {"name": "Rolf", "grade" : 90},
    {"name": "Bob", "grade" : 78},
    {"name": "Jen", "grade" : 100},
]

for student in students:
    #gets the name value (key) from the students dictionary
    name = student["name"] 
    #gets the grade value from the dictionary 
    grade = student["grade"] 
    
    print (f"{name} has a grade of {grade}.")
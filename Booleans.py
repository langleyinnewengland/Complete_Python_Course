#booleans should be equal to true
#age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150

#returns true of can_learn_programming is between 0-150.  False otherwise
print(f"You can learn programming: {can_learn_programming}.")

#determine if you are of working age
age = int(input("Enter your age: "))
usually_working = age >= 18 and age <=65

print(f"at {age}, you are usually not working: {usually_working}.")

#one or the other. This prints Mr. Smith because Name is an empty string
name = ""
surname = "Smith"

greeting = name or f"Mr. {surname}" #prints either name or surname.  since name is empty, it uses surname
print(greeting)

name = input("Enter your name: ")
surname = input("Enter your surname: ")

greeting = name or f"Mr. {surname}"
print (greeting)

#and gives you the first value if it is false, otherwise it gives you the 2nd value

#That's correct! The `or` keyword just returns the second value 
# if the first one evaluates to `False`.
# That's correct! If the value on the left of the `and` operator is truthy, 
# we get the value on the right of the operator.
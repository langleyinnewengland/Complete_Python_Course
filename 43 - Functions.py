#creating functions. Functions start with the def keyword
#syntax is def [function name]():


#define a new function called 'greet.  In the code below, the function
#gets defined, but it does not run

def greet ():
    name = input("Enter your name: ")
    print(f"Hello {name}")

#add a line to run he function (greet)
greet()

#variables created inside a function die outside of the function.  
#In the example above, name will not be a defined variable outside of the 'greet' function
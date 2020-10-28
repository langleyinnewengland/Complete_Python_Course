#enumerate joins a list with a number for each element is the list



#assign new variable 'name' to items in brothers list.
#first time through it prints 1st in list
#second time through in prints second in list. etc
brothers = ["Peter", "Ryan", "Carey"]
for name in brothers:
    print(name)

#to add an index
brothers = ["Peter", "Ryan", "Carey"]

counter = 0

for name in brothers:
    print(f"{counter} - {name}")
    counter = counter + 1 #incriments the index number by 1


#this does the same thing with the enumerate function

for counter, name in enumerate(brothers):
    print(f"{counter} - {name}")
  

#creates a lsit of tuples with name and counter number

print(list(enumerate(brothers)))

#this is the same as
print(list(zip([0, 1, 2], brothers)))

#make it a dictionary
print(dict(zip([0, 1, 2], brothers)))
#open a file in read mode
file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

#ignorel the first line in the file and white space
lines = [line.strip() for line in lines[1:]]

#iterate over lines
for line in lines:
    person_data=line.split(',') #seperates on the comma
    name = person_data[0]
    age = person_data[1]
    university=person_data[2]
    degree=person_data[3]

#print the data using an f-string
print(f'{name} is {age} studying {degree} at {university}')

\
#now fix the case
print(f'{name.title()} is {age} studying {degree.capitalize()} at {university.title()}')

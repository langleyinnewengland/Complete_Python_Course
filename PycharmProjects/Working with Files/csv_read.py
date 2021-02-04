file = open('csv_data.txt', 'r') #opens the file in read mode
lines = file.readlines() #reads the lines of the file
file.close() #closes the file

lines = [line.strip() for line in lines[1:]] #skips the first line as it is a header row also strips characters

for line in lines:
    person_data = line.split(',')
    name = person_data[0]
    age = person_data[1]
    university = person_data[2]
    degree=person_data[3]
print(f" {name} is {age} studying {degree} at {university}")
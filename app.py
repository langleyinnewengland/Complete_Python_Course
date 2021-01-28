opening and writing files in python

#open data.txt in read mode.  r= read mode
my_file = open('data.txt', 'r')
#read the file
file_content = my_file.read()
#print the contents
print(file_content)
#close  the file. Always close after opening
my_file.close()

#ask for name
user_name=input('enter your name: ')
#write to files w= write mode.  This will overwritre what exists in the file
my_file_writing = open('data.txt', 'w')
#write the user name to the data.txt file
my_file_writing.write(user_name)
my_file_writing.close()


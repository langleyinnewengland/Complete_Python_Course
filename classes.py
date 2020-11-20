def average_grade(student):
  return sum(student['grades']) / len(student['grades'])

class Student:
  def __init__(self, new_name, new_grades, new_school): #This line defines the items in the object
    self.name = new_name #defines the name property inside the self 
    self.grades = new_grades #creates the grades variable in the object
    self.school = new_school

  #this function is defined in the class, so it is a method
    def average(self):
        return sum(self.grades) / len(self.grades)
    #in metthods the first parameter is always called 'self'

student_one = Student('Rolf Smith', [70, 88, 90, 99], 'Rye Junior High')
student_two = Student('Peter Langley', [70, 100, 63, 99], 'North Hampton Elem')

print(student_one.name)
print(student_two.grades)
print(student_two.average())
print(student_two.school)

#a variable defined inside an object is called a property of the object
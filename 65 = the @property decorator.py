def average_grade(student):
  return sum(student['grades']) / len(student['grades'])

class Student:
  def __init__(self, new_name, new_grades, new_school): #This line defines the items in the object
    self.name = new_name #defines the name property inside the self
    self.grades = new_grades #creates the grades variable in the object
    self.school = new_school
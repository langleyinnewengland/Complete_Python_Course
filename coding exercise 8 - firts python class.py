


def average_grade(student):
  return sum(student['grades']) / len(student['grades'])



my_student = {
  'name': 'Rolf Smith',
  'grades': [70, 88, 90, 99],
  'average': 0 # something here to calculate
}


class Student:
  def __init__(self, new_name, new_grades): #self is the python name for a blank (initial) object -
    self.name = new_name #the .name defines the name variable in the empty self object
    self.grades = new_grades #creates the grades variable in the object

  def average(self):
    return sum(self.grades) / len(self.grades)

"""
Scary syntax! Don’t worry—what it does is close to the same.

When you have that class, you can create objects using it. Let’s do that first and then explain exactly what is happening:
"""

student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

"""
To create a new object, we use the class name as if it were a function call: `Student()`.

Inside the brackets, we put arguments that will map to the `__init__` method in the `Student` class.

`Student('Rolf Smith', [70, 88, 90, 99])` maps to `__init__(self, new_name, new_grades)`.

What you end up with is a /thing/ that has two properties, `name` and `grades`.
"""

print(student_one.name)
print(student_two.name)

"""
Inside the `__init__` method, we use `self.name` and `self.grades`. `self` is the current object, so when we assign values we modify only the “current object”.
"""

Student('Rolf Smith', [70, 88, 90, 99])

# def __init__(self, new_name, grades):
#  self.name = new_name
#  self.grades = new_grades

"""
When you do this, `self` is the new object you are creating. You can assign it to a variable:
"""

student_one = Student('Rolf Smith', [70, 88, 90, 99])

"""
As you do that more, every object is a different `self`,  with differently assigned properties depending on what you passed to the `Student()` /constructor/ call.
"""

## Properties

"""
Cool, so now we have the objects, both of which have different properties:
"""

student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

"""
These are _similar_ to our dictionaries, in that the dictionaries also store values:
"""

d_student_one = {
  'name': 'Rolf Smith',
  'grades': [70, 88, 90, 99]
}
d_student_two = {
  'name': 'Jose',
  'grades': [50, 60, 99, 100]
}

"""
To access them:

```
student_one.name
student_one.grades

student_two.name
student_two.grades

d_student_one['name']
d_student_one['grades']

d_student_two['name']
d_student_two['grades']
```
"""

## Methods

"""
> A method is a function which lives in a class.

The `average()` method in the Student () class also has access to `self`, the current object. When we call the method:
"""

print(student_one.average())

"""
What is really happening in the background is:
"""

print(Student.average(student_one))

"""
As you can see, `student_one` is passed as the first argument (and that is what `self` is in the method definition):
"""

def average(self):
  return sum(self.grades) / len(self.grades)

"""
So again, because `self` is `student_one`, `self.grades` is `student_one.grades`.

Thus:

* The sum of `self.grades` is the sum of `[70, 88, 90, 99]`: 347.
* The length of `self.grades` is 4.

The result will be `86.75`.
"""

## Recap

"""
Just to recap, the class is very similar to the dictionary but it allows us to include methods as well that have access to the properties of the object we created.

Classes also gives us a bunch more functionality, we’ll look at that in the coming videos!
"""
print(student_one.__class__)

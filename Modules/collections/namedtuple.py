
from collections import namedtuple
# ClassName = namedtuple('ClassName', ['field1', 'field2', 'field3'])

Point = namedtuple('Point', ['x', 'y'])
Circle = namedtuple('Circle', ['center', 'radius'])
Student = namedtuple('Student', ['name', 'age', 'grade'])

# declaration
p1 = Point(10, 20) 
c1 = Circle(Point(0, 0), 5)
s1 = Student("Alice", 20, "A")

# Accessing 
print(p1.x, p1[1])
print(c1.center.x)
print(s1.name, getattr(s1, 'age'))  

# Unpacking
x, y = p1
print("Unpacked values:", x, y)

# Methods
p2 = p1._replace(x=15) # Copy x , with edited value
print("Replaced Point:", p2)

s2 = s1._asdict()  # Convert to dictionary
print("Student as dict:", s2)

print("Field names:", Point._fields) # if you want to see field names

new_student = ["Belal", 20, "B"]
s3 = Student._make(new_student)  # Create from iterable 
print("New Student:", s3)

# s1.grade = "A+"  # raise AttributeError
s1 = s1._replace(grade="A+") # How to update 
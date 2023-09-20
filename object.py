# creating an Object
# All classes have a function called __init__(), which is always executed when the class is being initiated.
class MyName:
   def __init__(self, name, age):
    self.name = name
    self.age = age
# The __str__() function controls what should be returned when the class object is represented as a string.                                                       
    def __str__(self):
      (f"{self.name}is now {self.age}")
    # create object this is an object example:

p1 = MyName("Toby",21)
print(p1)

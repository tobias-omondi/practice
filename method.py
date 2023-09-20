class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

    def myfunc(self):
        print(f"Hello my dog is {self.name}")

dog= Dog("Junior",8)
dog.myfunc()
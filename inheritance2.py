# creating both parents and child class/super()
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        # method
    def printname(self):
        print(f"my name is {self.firstname} {self.lastname}" )

    def printme(self):
        print(f"i love {self.firstname} and {self.lastname}")
    # creating object
    
person = Person("Tobias","Ogolla")
person.printname()

food = Person("fish","Ugali")
food.printme()

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function

class Family(Person):
   # Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
     def __init__(self, fname, lname, year):
         super().__init__(fname, lname)
         self.birthday = year
     def congratulation(self):
         print(f"Happy birthday {self.firstname} {self.secondname} for turning 20")

x = Family("Tobias","Ogolla",2002)
Family()


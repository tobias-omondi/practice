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
     def __init__(self, fname, lname, age):
         super().__init__(fname, lname) 
         self.age =age
     def birthday(self):
         print(f"Happy Birthday {self.firstname} {self.lastname} for turning {self.age}")

toby = Family("Tobias" ,"Ogolla", 21)
toby.printname()
toby.birthday()

family = Family("Morgan","Jones", 20)
family.printname()

print(family.family)


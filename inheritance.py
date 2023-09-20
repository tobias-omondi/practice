# python inherantance
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

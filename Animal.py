# Inheritance practise

class Animal:
    alive = True
    def eat(self):
        print("The animal is eating")
    def sleep(self):
        print("The animal is sleeping")

class Rabbit(Animal):
    pass
class Cat(Animal):
    pass
class Lion(Animal):
    pass
class Fish(Animal):
    pass

rabbit = Rabbit()
cat = Cat()
lion =Lion()

print(Rabbit.alive)
cat.eat()
lion.sleep()
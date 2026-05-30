'''
class Animal:
    def sound(self):
        print("Some generetic animal sound")

class Dog(Animal):
    def sound(self):
        print("Wouf")


class Cat(Animal):
    def sound(self):
        print("Meow")

animal=Animal()

animal.sound()

pitbull = Dog()
pitbull.sound()

chiwawa = Dog()
chiwawa.sound()

british = Cat()
british.sound()
'''

'''
class Vertebrate:
    def __init__(self, backbone=True):
        self.has_backbone = backbone

    def vertebrate_info(self):
        print("Vertebrates have a backbone.")


class Aquatic:
    def __init__(self, habitat="water"):
        self.habitat = habitat

    def aquatic_info(self):
        print("Aquatic animals live in water.")


class Fish(Vertebrate, Aquatic):
    def __init__(self, species, backbone=True, habitat="water"):
        super().__init__(backbone=backbone)
        self.habitat = habitat
        self.species = species

    def fish_info(self):
        print(f"The {self.species} is a type of fish found in {self.habitat}.")

    def swim(self):
        print("The fish is swimming.")


goldfish = Fish("Goldfish")
print(goldfish.has_backbone)
print(goldfish.habitat)
goldfish.vertebrate_info()
goldfish.aquatic_info()
goldfish.fish_info()
goldfish.swim()
'''

'''
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sound(self):
        print(f"{self.name} makes the sound woof and its aged {self.age}")

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        def sound(self):
            print(f"{self.name}makes the sound meoww and its aged {slef.age}")



pitbulli = Dog('Buddy', 12)

pitbulli.sound()

british= Cat('Christina', 10)
british.sound()
'''


class Student:
    def __init__(self,name,grade):
        self.name= name
        self.grade= grade

    def introduce(self):
          print(f"Name: {self.name}, Grade: {self.grade}")


class PrimaryStudent(Student):
    def study(self):
        print(f"{self.name} po meson msimet baze me noten mesatare {self.grade}.")


class HighShcoolStudent(Student):
    def study(self):
        print(f"{self.name} po meson msimet e renda")

ylli = PrimaryStudent('YLLI',12)
ylli.study()

kroni = HighShcoolStudent('Kroni', 11)
kroni.study()
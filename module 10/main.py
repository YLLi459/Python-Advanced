class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name


    def set_name(self, name):
        return  self.__name


    def get_age(self):
        return self.__age


    def set_age(self, age):
        self.__age = age


student1 = Student("Alice", 17)


print("Name:", student1.get_name())
student1.set_name("Bob")
print("Updated Name:", student1.get_name())

print("Age:", student1.get_age())
student1.set_age(18)
print("Updated Age:", student1.get_age())



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return  3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


circle_1 = Circle(7)
square_1 = Square(10)

print(circle_1.area())
print(square_1.area())
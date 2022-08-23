from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError("Name must be at least 3 chars")
        self.__name = value

    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        return "Meow"

class Dog(Animal):
    def sound(self):
        return "Bark"
    def walk(self):
        return "walking"

cat = Cat("Pipi")
print(cat.name)
dog = Dog("Sharo")
print(dog.name)
print(cat.sound())
print(dog.walk())




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        pass


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise Exception("Age must be greater than zero")
        self.__age = value

    # def set_age(self, age_value):
    #     if age_value <= 0:
    #         raise Exception("Age must be greater than zero")
    #     self.__age = age_value

p = Person("Ben", 30)
p.age = 20
p.name = "Tom"
print(p.age)
print(p.name)
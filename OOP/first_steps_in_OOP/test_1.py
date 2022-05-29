
class Car:
    def __init__(self, name:str, model:str, engine):
        self.engine = engine
        self.model = model
        self.name = name


    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"

car = Car("Kia", "Rio", "1.3L 83 I4")
sport_car = Car("", "", "")
print(car.get_info())
print(sport_car.get_info())

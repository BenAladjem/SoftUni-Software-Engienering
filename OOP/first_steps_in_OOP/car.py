class Car:
    def __init__(self, name : str, model : str, engine : str):
        self.name = name
        self.model = model
        self.engine = engine
    def get_info(car):
        return f"This is {car.name} {car.model} with engine {car.engine}"
car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())

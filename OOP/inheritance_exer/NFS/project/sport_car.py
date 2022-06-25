from project.car import Car

class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10
    def __init__(self, fuel, horse_pover):
        super().__init__(fuel, horse_pover)
from project.motorcycle import Motorcycle

class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8
    def __init__(self, fuel, horse_pover):
        super().__init__(fuel, horse_pover)
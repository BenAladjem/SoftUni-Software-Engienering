class Vehicle:
    def __init__(self, mileage, max_speed = 150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []

    def move(self, m):
        self.mileage += m
        print('Moving...')

car = Vehicle(20,49)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
print(car.move(6), car.mileage)





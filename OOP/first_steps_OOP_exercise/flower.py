class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def status(self):
        if self.is_happy:
            res = f"{self.name} is happy"
        else:
            res = f"{self.name} is not happy"
        return  res

    def water(self, quantity):
        if self.water_requirements <= quantity:
            self.is_happy = True
        return self.is_happy



# flower = Flower("Lilly", 100)
# flower.water(50)
# print(flower.status())
# flower.water(60)
# print(flower.status())
# flower.water(100)
# print(flower.status())

        
        

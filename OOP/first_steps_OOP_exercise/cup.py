class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, param):
        if self.status() >= param:
            self.quantity += param


    def status(self):
        stat = self.size - self.quantity
        return stat



# cup = Cup(100, 50)
# print(cup.status())
# cup.fill(40)
# cup.fill(20)
# print(cup.status())

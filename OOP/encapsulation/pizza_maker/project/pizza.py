from project.topping import Topping


class Pizza:
    def __init__(self, name, dough, topping_capacity, toppings):
        self.topping_capacity = topping_capacity
        self.name = name
        self.dough = dough
        self.toppings = toppings

    def add_topping(self, topping: Topping):
        pass

    def calculate_total_weight(self):
        pass
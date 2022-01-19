class Vehicle:
    def __init__(self, vehicle_type:str, model: str, price: int):
        self.model = model
        self.price = price


    def buy(self, money: int, buyer:str):
        if self.price > money:
            return  'Sorry, not enough money'
        elif self.owner is not None:
            return 'Car already sold'
        else:
            return 'Vehicle has no owner'


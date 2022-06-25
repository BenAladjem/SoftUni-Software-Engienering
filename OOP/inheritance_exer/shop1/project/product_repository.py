from project.drink import Drink
from project.food import Food


class ProductRepository:
    def __init__(self):
        #self.name = name
        #self.quantity = quantity
        self.products = []

    def add(self, product):
        if not product in self.products:
            self.products.append(product)

    def find(self, product_name):
        products_with_that_name = [product.name for product in self.products if product.name == product_name]
        if products_with_that_name:
            return products_with_that_name[0]


    def remove(self, product_name):
        products_with_that_name = [product.name for product in self.products if product.name == product_name]
        if products_with_that_name:
            self.products.remove(products_with_that_name[0])


    def __repr__(self):
        for product in self.products:
            print(f"{product.name}: {product.quantity}")

apple = Food("apple")
d1 = Drink("kola")
d2 = Drink("water")
p_r = ProductRepository()
p_r.add(d1)
#p_r.add(d2)
p_r.add(apple)
p_r.find('cola')

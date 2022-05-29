class Person:
    def __init__(self, name, kg):
        self.name = name
        self.kg = kg

    def eat(self, amount):
        self.kg += amount

Tom = Person("Tomi", 50)
Tom.eat(2)
print(Tom.kg)

class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
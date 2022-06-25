from  project.mammal import Mammal
from project.lizard import Lizard

lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)


from Animal import Animal

class Lion(Animal):
  def __init__(self,name,age,health,happiness,power):
    super().__init__(name,age,health,happiness)
    self.power = 100
  def displat_info(self):
    print(f"name: {self.name} age : {self.age} health : {self.health} happiness : {self.happiness} power : {self.power}")
  

# semba = Lion("semba", 32,40,22, 94)

# semba.display_info()
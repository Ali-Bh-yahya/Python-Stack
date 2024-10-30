class Animal:
  def __init__ (self, name , age , health , happiness):
    self.name = name
    self.age = age
    self.health = health
    self.happiness = happiness
  
  def display_info (self):
    print(f"name : {self.name}, age : {self.age} , health : {self.health} , happiness : {self.happiness}")

  def feed(self):
    self.happiness += 10
    self.health += 10

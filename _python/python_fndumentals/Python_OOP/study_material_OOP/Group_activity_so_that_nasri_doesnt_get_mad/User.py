class User:
  def __init__(self,name,address,email,phone):
    self.name = name
    self.address = address
    self.email = email
    self.phone = phone
  
  def print_info(self):
    print(f"{self.name} {self.address} {self.email} {self.phone}")
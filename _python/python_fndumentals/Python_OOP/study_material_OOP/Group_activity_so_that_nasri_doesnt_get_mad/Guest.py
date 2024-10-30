from User import User

class Guest(User):
  def __init__(self,name,address,email,phone,visit_duration ):
    super().__init__(name, address, email, phone)
    self.visit_duration = visit_duration
  
  def display_info(self):
    print(f"{self.visit_duration}")

Ali = Guest("Ali","GAZA","ali@omar.com","0598033349","4 hours")

Ali.display_info()
from User_p import User

class Cuostomer(User):

  def __init__(self,name,address,phone,email,points,credit):
    super().__init__(name,address,phone,email)
    self.points = points
    self.credit = credit

  def print_points(self):
    print(f"the number of points is: {self.points}")
    

Ali = Cuostomer("Ali","WB","0593322640","ALi@gmail.ru",3000,4323)
Ali.print_user_name()
Ali.print_points()

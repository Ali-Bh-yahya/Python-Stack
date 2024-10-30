from User_p import User
class Employee(User):
  def __init__(self,name,address,phone,email,salary):
    super().__init__(name,address,phone,email)  # Call the parent class constructor.
    self.salary =salary

  def print_salary(self):
    print(f"your salary is : {self.salary}")

Izz = Employee('Izz',"RUS","0593322640","Izz@gmail.com",4500)
Izz.print_salary()
Izz.print_user_name()
class User:
  #1-including the __init__ and make_deposit methods
  def __init__ (self,name,email):
    self.name = name
    self.email = email
    self.balance = 0

  def make_deposit(self, amount):
    self.balance += amount
    return self
  
  #2-Add a make_withdrawal method to the User class
  # have this method decrease the user's balance by the amount specified
  def make_withdrawal(self , amount):
    self.balance -=amount
    return self
#3-display_user_balance(self) - have this method 
# print the user's name and account balance to the terminal
  def display_user_balance(self):
    print(f"{self.name} has {self.balance}$")

ali = User("Ali", "ali@gmail.com")
yazan = User("yazan","yazan@gmail.com")
izz = User("izz","izz@gmail.com")
#Have the Ali make 3 deposits and 1 withdrawal and then display their balance:
ali.make_deposit(1000).make_deposit(4000).make_deposit(3000).make_withdrawal(2000).display_user_balance()
#Have the yazan make 2 deposits and 2 withdrawals and then display their balance:
yazan.make_deposit(1000).make_deposit(4000).make_withdrawal(2000).make_withdrawal(1500).display_user_balance()

#Have the Izz make 1 deposit and 1 withdrawal and then display their balance:
izz.make_deposit(1000).make_withdrawal(500).make_withdrawal(500).make_withdrawal(500).display_user_balance()
class Bank_account:
  def __init__(self,int_rate, balance):
    self.int_rate = int_rate
    self.balance =balance

  def deposit(self,amount):
    self.balance += amount
    return self
  
  def withdraw(self,amount):
    self.balance -= amount
    return self
  
  
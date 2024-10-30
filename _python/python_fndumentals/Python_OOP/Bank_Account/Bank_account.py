class Bank_account:
  def __init__(self,int_rate):
    self.int_rate = int_rate
    self.balance =0
  def deposit(self,amount):
    self.balance +=amount
    return self
  def withdraw(self,amount):
    self.balance -=amount
    return self
  def display_account_info(self):
    print(f"{self.int_rate} and the balance is ${self.balance}")
  def yield_interest(self):
    interset = self.balance *self.int_rate
    self.balance += interset
    return self
    

account_ali = Bank_account(70.55)
account_ayman =Bank_account(30.40)

account_ali.deposit(1000).deposit(1000).deposit(5000).withdraw(2000).yield_interest().display_account_info()
account_ayman.deposit(2000).deposit(2000).withdraw(2000).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()
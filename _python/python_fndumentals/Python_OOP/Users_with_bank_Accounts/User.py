from Bank_account import Bank_account
class User:
  def __init__ (self,name,email):
    self.name = name
    self.email =email
    self.accounts = []
    self.accounts.append(Bank_account(int_rate=0.2,balance =0))

  def add_account(self):
    self.accounts.append(Bank_account(int_rate=0.2,balance =10))
    print(f"{self.name} has new account{self.accounts}")
  def remove_account(self,index):
    self.accounts.pop(index)
    print(f"{self.name} has removed account{self.accounts}")

  def display_user_info(self):
      print(f"name:{self.name} , email:{self.email}")

  def display_accounts(self):
    print(f"{self.name} has accounts")
    for i in range(len(self.accounts)):
      print(f"Account {i+1}: {self.accounts[i].balance}")
  

Ali = User("ali","ali@yndex.ru")
Omar = User("omar","omar@gmail.com")

Ali.add_account()
Ali.accounts[0].deposit(1100).withdraw(200)
Ali.display_user_info ()
Ali.display_accounts ()
Ali.remove_account(1)
print("\n")
Omar.add_account()
Omar.accounts[1].deposit(3000)
Omar.display_user_info()
Omar.display_accounts()
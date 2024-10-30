class User:

  def __init__(self,name,address,phone,email):
    self.name= name
    self.adderess = address
    self.phone = phone
    self.email = email
  def print_user_name(self):
    print(f'User Name: {self.name} , Email: {self.email} , Phone: {self.phone} and addresses: {self.adderess}')
  
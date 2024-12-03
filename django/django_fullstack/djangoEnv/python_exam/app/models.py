from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def validate_registration(self, post_data):
        errors = {}
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Invalid email address!'
        if len(post_data['first_name']) < 2:
            errors['first_name'] = 'First name should be at least 2 characters.'
        if len(post_data['last_name']) < 2:
            errors['last_name'] = 'Last name should be at least 2 characters.'
        if len(post_data['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters.'
        if post_data['password'] != post_data["confirm_PW"]:
            errors['password_dont_match'] = 'Password and confirm password must match!'
        return errors

    def login_validator(self,postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = 'Invalid email address!'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters.'
        email = postData['email']
        user = User.objects.filter(email=email).first()
        if not user:
            errors['email'] = "No user account with this email address was found."
            return errors
        else:
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "Incorrect password."
                return errors
        return errors
class PiesManager(models.Manager):
  def pies_validate(self , data):
      name_pie = data['name_pie']
      errors = {}
      if len(data['name_pie']) < 2:
          errors['name_pie'] = "the name should be at least 2 characters"
      if len(data['filling']) < 2:
          errors['filling']= "the filling should be at least 2 characters"
      if len(data['crust']) < 2:
        errors['crust']= "the crust should be at least 2 characters"
      if not Pies.objects.filter(name_pie = name_pie).exists:
          errors['name_pie'] = 'the name of the pie should be unique'
      return errors
          
class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #pieses = models.ForeignKey(Pies , related_name = 'users')

class Pies(models.Model):
    name_pie = models.CharField(max_length = 29,unique=True)
    filling = models.CharField(max_length = 50)
    crust = models.CharField(max_length = 50)
    users = models.ForeignKey(User, related_name='pies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PiesManager()
    


def save_data_for_reg(data):
    pw_hash = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()).decode()
    User.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=pw_hash
    )
# def get_data_Users(data):
#    return User.objects.all()


def save_data_for_pies(data, session):
    name_pie = data['name_pie']
    filling = data['filling']
    crust = data['crust']
    user = User.objects.get(id=session['user_id'])
    if not Pies.objects.filter(name_pie = name_pie).exists():
      Pies.objects.create(name_pie=name_pie , filling=filling , crust=crust , users=user)

def get_pies():
   pies = Pies.objects.all()
   return pies

def get_pies_by_baker(user_id):
    return Pies.objects.filter(users=User.objects.get(id=user_id))

def get_pie_by_id(pie_id):
    return Pies.objects.get(id = pie_id)

def delete_pie(pie_id):
  pies = Pies.objects.get(id=pie_id)
  pies.delete()
  return pies

def update_pies(data):
  id = int(data['id'])
  c=Pies.objects.get(id=id)
  c.name_pie = data['name_pie']
  c.filling = data['filling']
  c.crust = data['crust']
  c.save()
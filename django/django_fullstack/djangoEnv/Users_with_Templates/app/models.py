from django.db import models


# Create your models here.
class User(models.Model):
  fname = models.CharField(max_length=30)
  lname = models.CharField(max_length=30)
  email = models.EmailField()
  age = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


def insert_user(data):
  User.objects.create(fname =data['fname'],lname=data['lname'],email=data['email'],age = data['age'])


def add_data():
  users = User.objects.all()
  return users

def remove_user(id):
  user = User.objects.get(id=id)
  user.delete()
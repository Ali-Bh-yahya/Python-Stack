from django.db import models

# Create your models here.
class Dojo(models.Model):
  name = models.CharField(max_length=25)
  city = models.CharField(max_length=32)
  state =models.CharField(max_length = 225 )
  desc = models.CharField(max_length=22)

class Ninja(models.Model):
  first_name = models.CharField(max_length=233)
  last_name = models.CharField(max_length=224)
  dojo = models.ForeignKey(Dojo,related_name= "ninja" , on_delete = models.CASCADE)

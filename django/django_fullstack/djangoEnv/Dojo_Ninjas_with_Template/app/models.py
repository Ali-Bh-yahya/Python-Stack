from django.db import models

# Create your models here.
class Dojo(models.Model):
  name = models.CharField(max_length=25)
  city = models.CharField(max_length=32)
  state =models.CharField(max_length = 25 )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Ninja(models.Model):
  first_name = models.CharField(max_length=233)
  last_name = models.CharField(max_length=224)
  dojo = models.ForeignKey(Dojo,related_name= "ninjas" , on_delete = models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

 

def get_dojos():
  dojos =Dojo.objects.all()
  return dojos

def create_dojo(data):
    dojos = Dojo.objects.create( name = data["name"] , city = data["city"] , state =data["state"] )
    return dojos


def create_ninja(data):
    ninja = Ninja.objects.create( first_name = data["first_name"] , last_name = data["last_name"] , dojo =Dojo.objects.get(id=int(data["dojo"])))
    return ninja

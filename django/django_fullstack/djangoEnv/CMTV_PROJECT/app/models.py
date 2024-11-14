from django.db import models

# Create your models here.
class Show(models.Model):
  title = models.CharField(max_length=20)
  network =models.CharField(max_length=10)
  released_date = models.DateField()
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

def get_all_shows():
  return Show.objects.all()

def get_show_by_id():
  return Show.objects.get(id=id)

def create_show(data):
  title = data["title"]
  network = data['network']
  released_date = data['released_date']
  description = data['description']
  Show.objects.create(title=title, network=network, released_date=released_date, description=description)

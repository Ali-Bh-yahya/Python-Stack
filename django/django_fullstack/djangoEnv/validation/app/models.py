from django.db import models

# Create your models here.
class BlogManager(models.Manager):##Django models come with a built-in objects (manager) that we use for querying the database
  def basic_validation(self,post_data):
    errors = {}
    if len(post_data['name']) < 5 :
      errors["name"] = "Blog name should be at least 5 characters"
    if len(post_data['desc']) < 10 :
      errors['desc'] = "Blog descriptins should be at least 10 characters"
    return errors

class Blog(models.Modle):
  name = models.CharField(max_length = 22)
  desc = models.TextField( )
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now= True)  
  objects = BlogManager() ##Link the Custom Manager to the Model##




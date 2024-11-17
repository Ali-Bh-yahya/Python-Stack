from django.db import models

# Create your models here.
class Description(models.Model):
  content = models.TextField()

class CourseManager(models.Manager):
  def validate(self,post_data):
    errors = {}
    if len(post_data['course_name']) < 5:
      errors['course_name'] = 'Course name should be at least 5 characters long'
    if len(post_data['description']) < 15 :
      errors['description'] = 'Description should be at least 15 characters long'
    return errors
class Course(models.Model):
    course_name = models.CharField(max_length=100)  
    description = models.OneToOneField(Description, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

def create_course(data):
  return Course.objects.create(course_name = data['course_name'],  description = data['description'])


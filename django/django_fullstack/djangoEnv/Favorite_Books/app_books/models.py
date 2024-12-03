from django.db import models
from app_users.models import User
# Create your models here.
class BookManager(models.Manager):
    def validation_book(self, postdata):
        errors = {}
        if len(postdata['title']) < 1:
            errors['title'] = "please fill your title"
        if len(postdata['description']) < 5 :
            errors['description'] = "description must be at least 5 characters"

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded")
    users_who_like = models.ManyToManyField(User , related_name = "liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()


def create_books(data, session):
    Book.objects.create(title = data['title'], description = data['description'],uploaded_by = session['user'],user_who_like = session['user'])
def get_books():
    return Book.objects.all()
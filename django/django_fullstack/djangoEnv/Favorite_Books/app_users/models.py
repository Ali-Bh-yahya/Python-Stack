from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def validate_registration(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
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
        email = postData['email']
        user = User.objects.get(email=email)
        if not user:
            errors['email'] = "No user account with this email address was found."
        else:
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "Incorrect password."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


def save_data_for_reg(data):
    pw_hash = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()).decode()
    User.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=pw_hash
    )

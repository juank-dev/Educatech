from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    city = models.CharField(max_length=32, null=True)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

   
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(Subject, related_name='subject_teacher')

    def __str__(self):
        return self.user.username

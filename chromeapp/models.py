from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    fromchrome = models.BooleanField(null=True)

class Todo(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    duedate = models.DateTimeField()
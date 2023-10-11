from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    fromchrome = models.BooleanField(null=True)


class Todo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=10485760)
    duedate = models.DateTimeField()


class WebsiteMonitor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    view_time = models.JSONField()
    viewed_date = models.DateField(blank=False, default=timezone.now)

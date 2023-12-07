from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    num_guests = models.PositiveIntegerField()
    date = models.DateTimeField()
    content = models.TextField()

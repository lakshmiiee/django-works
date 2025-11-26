from django.db import models


# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=50)

class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
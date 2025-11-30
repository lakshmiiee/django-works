from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(max_length=3)
    grade=models.IntegerField(max_length=2)
from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    score=models.DecimalField(max_digits=3,decimal_places=2)

    

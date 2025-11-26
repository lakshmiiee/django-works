from django.db import models

# Create your models here.

class Teachers(models.Model):
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)

    

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255)
    pwd = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Data(models.Model):
    amount =  models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.description} - {self.amount}" 

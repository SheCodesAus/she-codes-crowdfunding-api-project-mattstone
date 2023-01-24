from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    title=models.CharField(max_length=200)
    pass 
    
    def __str__(self):
        return self.username

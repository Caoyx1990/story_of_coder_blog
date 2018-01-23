from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  telephone = models.CharField(max_length=20)
  email = models.EmailField()
  identity = models.CharField(max_length=50)
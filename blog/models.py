from django.db import models
from user.models import User

# Create your models here.
class Tag(models.Model):
  tag = models.CharField(max_length=100)

class Category(models.Model):
  category = models.CharField(max_length=100)

class Post(models.Model):
  title = models.CharField(max_length=200)
  author = models.OneToOneField(User)
  createTime = models.DateTimeField()
  changeTime = models.DateTimeField()
  category = models.ForeignKey(Category)
  tag = models.ManyToManyField(Tag)
  content = models.TextField()
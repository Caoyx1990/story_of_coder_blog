from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=150)
  createTime = models.DateTimeField()
  changeTime = models.DateTimeField()
  classify = models.CharField(max_length=100)
  tag = models.CharField(max_length=100)
  content = models.TextField()

class Tags(models.Model):
  tag = models.CharField(max_length=100)

class Classify(models.Model):
  classify = models.CharField(max_length=100)

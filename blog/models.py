from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=50)
  createTime = models.TimeField()
  changeTime = models.TimeField()
  classify = models.CharField(max_length=50)
  tag = models.CharField(max_length=50)
  content = models.TextField()

class Tags(models.Model):
  tag = models.ManyToManyField(Post.tag)

class Classify(models.Model):
  classify = models.ForeignKey(Post.classify)

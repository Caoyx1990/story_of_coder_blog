from django.db import models
from blog.models import Post
from user.models import User

# Create your models here.
class PostComments(models.Model):
  content = models.TextField()
  user = models.OneToOneField(User)
  post = models.ForeignKey(Post)

class UserComments(models.Model):
  content = models.TextField()
  comment = models.ForeignKey(PostComments)
  user = models.OneToOneField(User)

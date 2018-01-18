from django.shortcuts import render
from django.http import request, response
from blog.models import Post,Tags,Classify
from markdown import markdown  

# Create your views here.
def home(request):
  posts = Post.objects.all()
  for post in posts:
    post.content = markdown(post.content)
  tags = Tags.objects.all()
  classifys = Classify.objects.all()
  return render(request, "home.html", {'posts': posts, 'tags': tags, 'classifys': classifys})

def posts(request):
  category = '文章列表'
  classify = request.GET.get('classify')
  tag = request.GET.get('tag')
  if classify:
    category = Classify.objects.get(classify=classify)
    category = category.classify
  elif tag:
    category = Tags.objects.get(tag=tag)
    category = category.tag
  posts = Post.objects.all()
  for post in posts:
    post.content = markdown(post.content)
  tags = Tags.objects.all()
  classifys = Classify.objects.all()
  return render(request, "posts.html", {'category': category, 'posts': posts, 'tags': tags, 'classifys': classifys})

def post(request, post_id):
  blog_post = Post.objects.get(id=post_id)
  blog_post.content = markdown(blog_post.content)
  tags = Tags.objects.all()
  classifys = Classify.objects.all()
  return render(request, "post.html", {'post': blog_post, 'tags': tags, 'classifys': classifys})

def about(request):
  return render(request, "about.html")

def feature(request):
  return render(request, "posts.html")
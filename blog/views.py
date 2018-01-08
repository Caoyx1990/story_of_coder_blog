from django.shortcuts import render
from django.http import request, response

# Create your views here.
def home(request):
  return render(request, "home.html")

def posts(request):
  return render(request, "posts.html")

def post(request):
  return render(request, "post.html")

def about(request):
  return render(request, "about.html")

def feature(request):
  return render(request, "posts.html")
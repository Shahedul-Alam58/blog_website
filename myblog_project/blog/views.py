from django.shortcuts import render
from .models import Post  # import your model

def blog_home(request):
    posts = Post.objects.all()  # fetch all posts from database
    return render(request, "blog/home.html", {"posts": posts})

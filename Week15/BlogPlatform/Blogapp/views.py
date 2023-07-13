from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, "home.html")


def view_post(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "all_post.html", context)

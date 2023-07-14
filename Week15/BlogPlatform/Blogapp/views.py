from django.shortcuts import render
from .models import Post, Author


def home(request):
    return render(request, "home.html")


def view_post(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "all_post.html", context)


def view_authors(request):
    authors = Author.objects.all()
    context = {"authors": authors}
    return render(request, "all_author.html", context)

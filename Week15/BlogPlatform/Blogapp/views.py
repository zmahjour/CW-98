from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Comment


def home(request):
    return render(request, "home.html")


def view_post(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "all_post.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, "post_detail.html", {"post": post, "comments": comments})


def view_author(request):
    authors = Author.objects.all()
    context = {"authors": authors}
    return render(request, "all_author.html", context)


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, "author_detail.html", {"author": author})

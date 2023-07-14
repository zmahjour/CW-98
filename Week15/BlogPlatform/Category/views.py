from django.shortcuts import render, get_object_or_404
from .models import Category


def view_category(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "all_category.html", context)


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, "category_detail.html", {"category": category})

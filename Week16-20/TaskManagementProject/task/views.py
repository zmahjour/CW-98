from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import View
from django.views.generic import ListView
from .models import Task, Category, Tag
from .forms import TaskUpdateForm
from .mixins import TodoOwnerRequiredMixin


def home(request):
    tasks = Task.objects.all().order_by("-id")[0:4]
    return render(request, "home.html", {"tasks": tasks})


def search(request):
    if request.method == "GET":
        search = request.GET["search"]
        results = Task.objects.filter(
            Q(title__icontains=search) | Q(tags__label__icontains=search)
        ).distinct()

        return render(request, "search.html", {"search": search, "results": results})


class TaskDetailView(TodoOwnerRequiredMixin, View):
    form_class = TaskUpdateForm

    def get(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        form = self.form_class(instance=task)
        return render(request, "task_detail.html", {"task": task, "form": form})
    
    def post(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        if "tag_submit" in request.POST:
            label = request.POST.get("tag")
            if not Tag.objects.filter(label=label).exists():
                Tag.objects.create(label=label)
            tag = Tag.objects.get(label=label)
            task.tags.add(tag)

            return redirect("task_detail", task_id=task_id)

        if "update_submit" in request.POST:
            form = self.form_class(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("task_detail", task_id=task_id)
            return render(request, "task_detail.html", {"form": form})


def all_tasks(request):
    cat_list = Category.objects.all()
    tag_list = Tag.objects.all()
    status_choices = dict(Task.STATUS_CHOICES)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        file = request.POST.get("file")
        status = request.POST.get("status")
        category_id = request.POST.get("cat")
        category = Category.objects.get(pk=category_id)
        tag_id_list = request.POST.getlist("tags")
        tags = [Tag.objects.get(pk=tag_id) for tag_id in tag_id_list]

        new_task = Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            file=file,
            status=status,
            category=category,
        )
        new_task.tags.set(tags)
        return redirect("all_tasks")

    else:
        tasks = Task.objects.all().order_by("-id")
        return render(
            request,
            "all_tasks.html",
            {
                "tasks": tasks,
                "cat_list": cat_list,
                "tag_list": tag_list,
                "status_choices": status_choices,
            },
        )


class AllTasksView(ListView):
    model = Task
    template_name = "all_tasks.html"
    context_object_name = "tasks"
    ordering = "-id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_list"] = Category.objects.all()
        context["tag_list"] = Tag.objects.all()
        context["status_choices"] = dict(Task.STATUS_CHOICES)
        return context

def categories(request):
    if request.method == "POST":
        name = request.POST.get("category_name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        Category.objects.create(name=name, description=description, image=image)
        return redirect("categories")

    elif request.method == "GET":
        categories = Category.objects.all()
        return render(request, "categories.html", {"categories": categories})


def category_detail(request, category_id):
    tag_list = Tag.objects.all()
    status_choices = dict(Task.STATUS_CHOICES)
    category = Category.objects.get(pk=category_id)
    tasks = Task.objects.filter(category=Category.objects.get(pk=category_id))

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        file = request.POST.get("file")
        status = request.POST.get("status")
        tag_id_list = request.POST.getlist("tags")
        tags = [Tag.objects.get(pk=tag_id) for tag_id in tag_id_list]

        new_task = Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            file=file,
            status=status,
            category=category,
        )
        new_task.tags.set(tags)
        return redirect("category_detail", category_id=category_id)

    return render(
        request,
        "category_detail.html",
        {
            "category": category,
            "tag_list": tag_list,
            "status_choices": status_choices,
            "tasks": tasks,
        },
    )


def update_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == "POST":
        name = request.POST.get("category_name")
        description = request.POST.get("description")
        image = request.POST.get("image")
        Category.objects.filter(pk=category_id).update(
            name=name, description=description, image=image
        )
        return redirect("categories")

    elif request.method == "GET":
        return render(request, "category_detail.html", {"category": category})


def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect("categories")


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("all_tasks")

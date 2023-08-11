from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TodoForm


class TodoOwnerRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        if not request.user.is_authenticated:
            raise PermissionDenied
        if not task.user == request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
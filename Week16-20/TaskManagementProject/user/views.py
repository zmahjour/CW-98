from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = "user/login.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You logged in successfully!", "success")
                return redirect("home:home")
            messages.error(request, "Email or password is wrong!", "warning")
        return render(request, self.template_name, {"form": form})

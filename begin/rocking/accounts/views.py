from urllib import request
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from .decorators import student_required, teacher_required

# Create your views here.


@login_required
def account_home(request):
    if request.user.profile.role == "student":
        return render(request, "accounts/dashboard.html")
    elif request.user.profile.role == "teacher":
        return render(request, "accounts/dashboard.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("account_home")
            else:
                form.add_error(None, "Invalid username or password")

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"]
            )
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")

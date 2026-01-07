from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import profile


def student_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.profile.role != "student":
            return redirect("account_home")
        return view_func(request, *args, **kwargs)
    return wrapper


def teacher_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.profile.role != "teacher":
            return redirect("account_home")
        return view_func(request, *args, **kwargs)
    return wrapper

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def review_list(request):
    return render(request, 'reviews/review_list.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import submission
from .models import Reviews
from .forms import ReviewForm


@login_required
def submission_reviews(request, submission_id):
    sub = get_object_or_404(submission, id=submission_id)

    is_teacher = request.user == sub.assignment.teacher
    is_student = request.user == sub.student

    if not (is_teacher or is_student):
        return redirect('project_list')

    reviews = sub.reviews.all()

    if request.method == 'POST' and is_teacher:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.teacher = request.user
            review.student = sub.student
            review.submission = sub
            review.save()
            return redirect('submission_reviews', submission_id=sub.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/submission_reviews.html', {
        'submission': sub,
        'reviews': reviews,
        'form': form,
        'is_teacher': is_teacher
    })

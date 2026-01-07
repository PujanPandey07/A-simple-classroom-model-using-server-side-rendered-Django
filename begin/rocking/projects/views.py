from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import assignment, submission
from accounts.decorators import teacher_required, student_required
from .forms import AssignmentForm, SubmissionForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.


@login_required
def project_list(request):
    assignments = assignment.objects.all().filter(
        deadline__gte=timezone.now()).order_by('deadline')
    return render(request, "projects/project_home.html", {
        "assignments": assignments
    })


@login_required
@teacher_required
def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            new_assignment = form.save(commit=False)
            new_assignment.teacher = request.user
            new_assignment.save()
            messages.success(request, "Assignment submitted successfully!")

            return redirect('project_list')
        messages.error(request, "Please correct the errors below.")

    else:
        form = AssignmentForm()
    return render(request, 'projects/create_assignment.html', {'form': form})


@login_required
@student_required
def submit_assignment(request, assignment_id):
    assignment_instance = assignment.objects.get(id=assignment_id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            new_submission = form.save(commit=False)
            new_submission.assignment = assignment_instance
            new_submission.student = request.user
            new_submission.save()
            messages.success(request, "Submission successful!")
            return redirect('project_list')
    else:
        form = SubmissionForm()
    return render(request, 'projects/submit_assignment.html', {'form': form, 'assignment': assignment_instance})


@login_required
def assignment_detail(request, pk):
    Assignment = get_object_or_404(assignment, pk=pk)

    if Assignment.is_expired():
        return render(request, 'projects/expired.html')

    Submission = submission.objects.filter(
        assignment=Assignment,
        student=request.user
    ).first()

    return render(request, 'projects/assignment_detail.html', {
        'assignment': Assignment,
        'submission': Submission
    })

from .models import assignment, submission
from django import forms


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = assignment
        fields = ['title', 'description',
                  'deadline', 'refrence_link', 'ref_files']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = submission
        fields = ['content', 'file', 'drive_link']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }

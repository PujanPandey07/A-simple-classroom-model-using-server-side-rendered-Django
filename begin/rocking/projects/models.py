from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class assignment(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    refrence_link = models.URLField(blank=True, null=True)
    ref_files = models.FileField(
        upload_to='assignment_files/', blank=True, null=True)

    def is_expired(self):
        return timezone.now() > self.deadline

    def __str__(self):
        return self.title


class submission(models.Model):
    assignment = models.ForeignKey(
        assignment,
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    content = models.TextField(blank=True)
    file = models.FileField(
        upload_to='submission_files/', blank=True, null=True)
    drive_link = models.URLField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("assignment", "student")

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"

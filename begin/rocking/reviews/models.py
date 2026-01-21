from django.db import models
from django.contrib.auth.models import User


class Reviews(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='given_reviews'
    )
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_reviews'
    )
    submission = models.ForeignKey(
        'projects.submission', on_delete=models.CASCADE, related_name='reviews'
    )
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher.username} → {self.student.username}"

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class profile(models.Model):
    Role_choices = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10, choices=Role_choices, default='student')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

from django.db import models
from django.contrib.auth.models import User
from instructors.models import Instructor


class Course(models.Model):
    instructor = models.OneToOneField(Instructor, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    seats_count = models.Count
    level = models.TextChoices
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

from django.db import models
from django.contrib.auth.models import User

from categories.models import Category
from instructors.models import Instructor


class Course(models.Model):
    class Levels(models.TextChoices):
        BEGINNER = "beginner"
        INTERMEDIATE = "intermediate"
        ADVANCED = "advanced"
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="courses")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    start_date = models.DateField()
    end_date = models.DateField()
    seats_count = models.IntegerField()
    level = models.CharField(max_length=50, choices=Levels.choices, default=Levels.BEGINNER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.instructor}'s {self.category} course"

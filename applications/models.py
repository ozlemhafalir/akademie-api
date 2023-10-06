from django.db import models
from django.contrib.auth.models import User

from courses.models import Course


class Application(models.Model):
    class Status(models.TextChoices):
        NEW = "new"
        APPROVED = "approved"
        CANCELLED = "cancelled"

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="applications")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.NEW)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s application to {self.course}"

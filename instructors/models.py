from django.db import models
from django.contrib.auth.models import User

from profiles.models import Profile


class Instructor(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending"
        ACTIVE = "active"
        INACTIVE = "inactive"

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s instructor profile"

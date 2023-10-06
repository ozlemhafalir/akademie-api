from django.db import models
from django.contrib.auth.models import User
from instructors.models import Instructor


class Category(models.Model):
    slug = models.SlugField(max_length=200)
    image = models.ImageField(
        upload_to='images/', default=''
    )
    instructor = models.OneToOneField(Instructor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

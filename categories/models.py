from django.db import models
from django.contrib.auth.models import User
from instructors.models import Instructor


class Category(models.Model):
    slug = models.SlugField(max_length=200)
    name = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='images/', default=''
    )
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children", on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryList(generics.ListAPIView):
    """
    List categories
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'parent_id'
    ]


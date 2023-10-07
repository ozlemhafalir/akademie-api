from rest_framework import generics
from courses.models import Course
from courses.serializers import CourseSerializer


class CourseList(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDetail(generics.RetrieveUpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()



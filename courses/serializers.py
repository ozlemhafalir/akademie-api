from rest_framework import serializers
from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = [
            "id",
            "instructor",
            "category",
            "start_date",
            "end_date",
        ]

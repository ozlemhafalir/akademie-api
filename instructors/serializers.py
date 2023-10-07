from rest_framework import serializers
from instructors.models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = [
            'id',
            'profile',
            'slug',
        ]
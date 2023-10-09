from rest_framework import serializers
from instructors.models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    profile_image = serializers.ReadOnlyField(source='profile.image', allow_null=True)
    title = serializers.ReadOnlyField(source='profile.user.username')
    class Meta:
        model = Instructor
        fields = [
            'id',
            'profile_image',
            'slug',
            'title',
        ]

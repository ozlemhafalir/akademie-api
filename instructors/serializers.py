from rest_framework import serializers
from instructors.models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()
    title = serializers.ReadOnlyField(source='profile.owner.username')

    def get_profile_image(self, obj):
        return obj.profile.image if obj.profile.image else None
    class Meta:
        model = Instructor
        fields = [
            'id',
            'profile_image',
            'slug',
            'title',
        ]

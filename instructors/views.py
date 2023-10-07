from rest_framework import generics
from instructors.models import Instructor
from instructors.serializers import InstructorSerializer


class InstructorList(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.profile.instructor:
            serializer.save(profile=self.request.user.profile)


class InstructorDetail(generics.RetrieveAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()
    lookup_field = "slug"


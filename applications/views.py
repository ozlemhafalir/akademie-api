from rest_framework import generics
from applications.models import Application
from applications.serializers import ApplicationSerializer


class ApplicationList(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ApplicationDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()



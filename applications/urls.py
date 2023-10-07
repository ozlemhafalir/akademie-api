from django.urls import path
from applications import views

urlpatterns = [
    path('applications/', views.ApplicationList.as_view())
]

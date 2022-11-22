
from django.urls import path, include
from rest_framework import routers
from Api.views import StudentView


urlpatterns = [
    path("student", StudentView.as_view(), name="students-api"),
    path('student/<int:id>', StudentView.as_view()),  
    path('student/<int:id>/update', StudentView.as_view())  
]

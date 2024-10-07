# urls.py
from django.urls import path
from .views import projects, project_detail

urlpatterns = [
    path('', projects, name='projects'),
    path('/<int:pk>/', project_detail, name='project_detail'),  # Pastikan URL ini ada
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('<int:pk>/', views.response, name='response'),
]
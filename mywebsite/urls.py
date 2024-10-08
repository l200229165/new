from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profile.urls')),
    path('projects/', include('projects.urls')),
    path('contact/', include('contact.urls')),
]
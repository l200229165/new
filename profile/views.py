from django.shortcuts import render
from .models import Profile, Resume

def profile(request):
    profile = Profile.objects.first()  # Mengambil data profil pertama
    return render(request, 'profile/profile.html', {'profile': profile})

def resume(request):
    resume = Resume.objects.all()  # Mengambil semua data resume
    return render(request, 'profile/resume.html', {'resume': resume})

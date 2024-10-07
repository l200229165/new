from django.shortcuts import render, get_object_or_404
from .models import Project

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)  # Menggunakan get_object_or_404 untuk menangani proyek yang tidak ditemukan
    return render(request, 'projects/project_detail.html', {'project': project})

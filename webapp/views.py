from django.shortcuts import render

# View untuk halaman Home
def index(request):
    return render(request, 'webapp/index.html')

# View untuk halaman Resume
def resume(request):
    return render(request, 'webapp/resume.html')

# View untuk halaman Projects
def projects(request):
    return render(request, 'webapp/projects.html')

# View untuk halaman Contact
def contact(request):
    return render(request, 'webapp/contact.html')

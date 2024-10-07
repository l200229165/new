# projects/views.py

from django.shortcuts import render
from .models import Contact

def contact(request):
    contact = Contact.objects.all()  # Mengambil semua data proyek
    return render(request, 'contact/contact.html', {'contact': contact})

def response(request, pk):
    response = Contact.objects.get(pk=pk)  # Mengambil proyek berdasarkan primary key
    return render(request, 'contact/response.html', {'response': response})


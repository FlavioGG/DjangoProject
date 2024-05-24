from django.shortcuts import render

# Create your views here.

from . import models

def home(request):
    return render(request, 'users/home.html')

def about(request):
    return render(request, 'users/about.html')

def contact(request):
    return render(request, 'users/contact.html')

def projects(request):
    return render(request, 'users/projects.html')
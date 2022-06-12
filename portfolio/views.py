from django.shortcuts import render
from .models import Project

def home(request):
    proyects = Project.objects.all()
    return render(request, 'home.html', {'proyects':proyects})

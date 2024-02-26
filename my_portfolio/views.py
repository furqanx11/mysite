from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Project,About,Certification,Education,Skill

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def about(request):
    about = About.objects.first()
    return render(request, 'about.html', {'about': about})

def education(request):
    education = Education.objects.all()
    return render(request, 'education.html', {'education': education})

def certifications(request):
    certifications = Certification.objects.all()
    return render(request, 'certifications.html', {'certifications': certifications})

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})
import imp
from django.shortcuts import render
from .models import About, Experience, Education, Awards, Interests, Skill, Workflow
# Create your views here.


def home(request):
    about = About.objects.all()[0]
    experience = Experience.objects.all()
    education = Education.objects.all()
    awards = Awards.objects.all()
    skills = Skill.objects.all()
    interests = Interests.objects.all()[0]
    workflow = Workflow.objects.all()
    data = {
        'about': about,
        'experience': experience,
        'education': education,
        'awards': awards,
        'interests': interests,
        'skills': skills,
        'workflow': workflow,
    }
    return render(request, 'webpages/home.html', data)


def nav(request):
    about = About.objects.all()[0]
    data = {
        'about': about,
    }
    return render(request, 'includes/nav.html', data)

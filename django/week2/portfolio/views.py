from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """
    Renders home page.
    """
    context = {}
    return render(request, 'home.html', context)

def resume(request):
    """
    Renders resume page.
    """
    context = {}
    return render(request, 'resume.html', context)

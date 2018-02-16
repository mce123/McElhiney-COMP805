from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """
    Renders home page.
    """
    title = "Patrick R. McElhiney's Homepage"
    context = {'title':title}
    return render(request, 'home.html', context)

def resume(request):
    """
    Renders resume page.
    """
    context = {}
    return render(request, 'resume.html', context)

def portfolio(request):
    """
    Renders portfolio page.
    """
    title = "Patrick R. McElhiney's Portfolio"
    context = {'title':title}
    return render(request, 'portfolio.html', context)

def contact(request):
    """
    Renders contact page.
    """
    title = "Contact Patrick R. McElhiney"
    context = {'title':title}
    return render(request, 'contact.html', context)

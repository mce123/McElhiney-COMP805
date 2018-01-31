from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """
    Renders home page.
    """
    greeting = "uStudy - the best study site in the world!"
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    context = {'our_greeting':greeting, 'weekday_list':days_of_week}

    return render(request, 'home.html', context)

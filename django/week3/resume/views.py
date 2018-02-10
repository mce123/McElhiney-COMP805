from django.shortcuts import render
from .models import Education, Experience

def resume(request):
    """
    Renders resume page.
    """
    qs1 = Education.objects.order_by('id')
    qs2 = Experience.objects.order_by('id')
    context = {'education':qs1, 'experience':qs2}
    return render(request, 'resume.html', context)

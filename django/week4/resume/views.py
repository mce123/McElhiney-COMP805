from django.shortcuts import render
from .models import Qualification, Experience, Education, Certification

def resume(request):
    """
    Renders resume page.
    """
    qs1 = Education.objects.order_by('id')
    qs2 = Experience.objects.order_by('id')
    qs3 = Qualification.objects.order_by('id')
    qs4 = Certification.objects.order_by('-date_obtained')
    context = {'education':qs1, 'experience':qs2, 'qualification':qs3, 'certification':qs4}
    return render(request, 'resume.html', context)

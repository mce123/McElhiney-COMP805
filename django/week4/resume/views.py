from django.shortcuts import render, Http404
from .models import Resume, Qualification, Experience, Education, Certification

def resume(request):
    """
    Renders resume page.
    """
    resume_object = Resume.objects.get(pk=1)
    resumes = Resume.objects.order_by('id')
    context = {'resume_object':resume_object, 'resumes':resumes}
    return render(request, 'resume.html', context)

def by_id(request, get_id):
    """
    Renders resume page.
    """
    by_pkid = False
    by_email = False
    try:
        resume_object = Resume.objects.get(pk=get_id)
        by_pkid = True
    except ValueError:
        try:
            resume_object = Resume.objects.get(email=get_id)
            by_email = True
        except ValueError:
            raise Http404()
    resumes = Resume.objects.order_by('-id')
    context = {'resume_object':resume_object, 'resumes':resumes}
    return render(request, 'resume.html', context)

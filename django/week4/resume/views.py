from django.shortcuts import render, Http404
from .models import Resume, Qualification, Experience, Education, Certification

def resume(request):
    """
    Renders resume page.
    """
    this_object = Resume.objects.get(pk=1)
    full_name = Resume.get_full_name_wmi(this_object)
    full_name_wmi = Resume.get_full_name_wmi(this_object)
    full_name_wmn = Resume.get_full_name_wmn(this_object)
    selected_email = this_object.email
    title = full_name_wmi + "'s Resume"
    profile_statement = this_object.profile_statement
    qs0 = Resume.objects.order_by('last_name')
    qs1 = Education.objects.order_by('id')
    qs2 = Experience.objects.order_by('-end_date')
    qs3 = Qualification.objects.order_by('id')
    qs4 = Certification.objects.order_by('-date_obtained')
    context = {'title':title, 'selected_email':selected_email, 'resumes':qs0, 'profile_statement':profile_statement, 'education':qs1, 'experience':qs2, 'qualification':qs3, 'certification':qs4}
    return render(request, 'resume.html', context)

def by_id(request, get_id):
    """
    Renders resume by pk=id.
    """
    by_pkid = False
    by_email = False
    try:
        this_object = Resume.objects.get(pk=get_id)
        by_pkid = True
    except ValueError:
        try:
            this_object = Resume.objects.get(email=get_id)
            by_email = True
        except ValueError:
            raise Http404()
    
    full_name = Resume.get_full_name_wmi(this_object)
    full_name_wmi = Resume.get_full_name_wmi(this_object)
    full_name_wmn = Resume.get_full_name_wmn(this_object)
    selected_email = this_object.email
    title = full_name_wmi + "'s Resume"
    profile_statement = this_object.profile_statement
    qs0 = Resume.objects.order_by('last_name')
    qs1 = Resume.get_education(this_object).order_by('id')
    qs2 = Resume.get_experience(this_object).order_by('-end_date')
    qs3 = Resume.get_qualification(this_object).order_by('id')
    qs4 = Resume.get_certification(this_object).order_by('-date_obtained')
    context = {'title':title, 'selected_email':selected_email, 'resumes':qs0, 'profile_statement':profile_statement, 'education':qs1, 'experience':qs2, 'qualification':qs3, 'certification':qs4}
    return render(request, 'resume.html', context)

from django.contrib import admin
from .models import Resume, Qualification, Experience, Education, Certification

admin.site.register(Resume)
admin.site.register(Qualification)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Certification)

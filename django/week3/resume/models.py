from django.db import models

class Education(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Experience(models.Model):
    institution_name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    degree = models.CharField(max_length=255, null=False, blank=False)
    major = models.CharField(max_length=255, null=False, blank=False)
    gpa = models.FloatField()

    def __str__(self):
        return self.institution_name

    class Meta:
        ordering = ['institution_name']

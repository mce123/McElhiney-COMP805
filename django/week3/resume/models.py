from django.db import models

class Education(models.Model):
    institution_name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    degree = models.CharField(max_length=255, null=False, blank=False)
    major = models.CharField(max_length=255, null=False, blank=False)
    gpa = models.FloatField()

    def __str__(self):
        return self.institution_name

    class Meta:
        ordering = ['institution_name']

class Experience(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Qualification(models.Model):
    qual_type = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.qual_type

    class Meta:
        ordering = ['qual_type']

class Certification(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    date_obtained = models.DateField()
    status = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_obtained']

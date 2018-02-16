from django.db import models

class Resume(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    profile_statement = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['last_name']

    def get_full_name(self):
        '''
        Returns the full name of the first Resume model object self. i.e. Patrick McElhiney
        '''
        return self.first_name + " " + self.last_name

    def get_full_name_wmi(self):
        '''
        Returns the full name with middle initial of the first Resume model object self. i.e. Patrick R. McElhiney
        '''
        try:
            if self.middle_name != None:
                return self.first_name + " " + self.middle_name[0] + ". " + self.last_name
        except:
            return self.first_name + " " + self.last_name

    def get_full_name_wmn(self):
        '''
        Returns the full name with middle name of the first Resume model object self. i.e. Patrick Russell McElhiney
        '''
        try:
            if self.middle_name != None:
                return self.first_name + " " + self.middle_name + " " + self.last_name
        except:
            return self.first_name + " " + self.last_name

    def get_last_name_first_name(self):
        '''
        Returns the full name - last_name, first_name of the Resume model object self. i.e. McElhiney, Patrick
        '''
        return self.last_name + ", " + self.first_name

    def get_experience(self):
        '''
        Returns all Experience objects of the Resume model object self.
        '''
        return self.experience_set.all()

    def get_education(self):
        '''
        Returns all Education objects of the Resume model object self.
        '''
        return self.education_set.all()

    def get_qualification(self):
        '''
        Returns all Qualification objects of the Resume model object self.
        '''
        return self.qualification_set.all()

    def get_certification(self):
        '''
        Returns all Certification objects of the Resume model object self.
        '''
        return self.certification_set.all()

class Experience(models.Model):
    parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Education(models.Model):
    parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
    institution_name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    degree = models.CharField(max_length=255, null=False, blank=False)
    major = models.CharField(max_length=255, null=False, blank=False)
    gpa = models.FloatField()

    def __str__(self):
        return self.institution_name

    class Meta:
        ordering = ['institution_name']

class Qualification(models.Model):
    parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
    qual_type = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.qual_type

    class Meta:
        ordering = ['qual_type']

class Certification(models.Model):
    parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255, null=False, blank=False)
    date_obtained = models.DateField()
    status = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_obtained']

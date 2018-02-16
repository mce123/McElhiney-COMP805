from django.test import TestCase
from .models import Resume, Qualification, Experience, Education, Certification

class ResumeTestCase(TestCase):
    resume = None
    full_name = None
    last_name_first_name = None
    experience = None
    education = None
    qualifications = None
    certification = None

    def setUp(self): 
        ''' 
        Sets up our testing fixture and creates objects 
        which we can use in future tests 
        ''' 
        self.resume = Resume.objects.create(
                                                              first_name='Patrick',
                                                              middle_name='Russell',
                                                              last_name='McElhiney',
                                                              email='patrick@mce123.com'
                                                  ) 
        self.experience = Experience.objects.create( 
                                                              parent_resume=self.resume, 
                                                              title='Experience Testing Title',
                                                              location='Experience Testing Location',
                                                              start_date='2017-01-01',
                                                              end_date='2018-01-01',
                                                              description='Experience Testing Description'
                                                   ) 
        self.education = Education.objects.create( 
                                                              parent_resume=self.resume, 
                                                              institution_name='Education Testing Institution Name',
                                                              location='Education Testing Location',
                                                              degree='Education Testing Degree',
                                                              major='Education Testing Major',
                                                              gpa = 4.0
                                                 ) 
        self.qualifications = Qualification.objects.create( 
                                                              parent_resume=self.resume, 
                                                              qual_type='Qualification Testing Type',
                                                              description='Qualification Testing Description'
                                                          )
        self.certification = Certification.objects.create(
                                                              parent_resume=self.resume,
                                                              name='Certification Test Name',
                                                              date_obtained='2018-01-01',
                                                              status='Certification Test Status'
                                                         )

    def test_starting_conditions(self): 
        ''' 
        Check if models exist properly. 
        ''' 
        self.assertIsInstance(self.resume, Resume) 
        self.assertIsInstance(self.experience, Experience) 
        self.assertIsInstance(self.education, Education) 
        self.assertIsInstance(self.qualifications, Qualification)
        self.assertIsInstance(self.certification, Certification)

    def test_full_name(self): 
        ''' 
        Tests that the Resume.full_name() is equal to "Patrick McElhiney"
        ''' 
        self.assertEqual(Resume.get_full_name(self.resume), 'Patrick McElhiney')

    def test_last_name_first_name(self): 
        ''' 
        Tests that the Resume.last_name_first_name() is equal to "McElhiney, Patrick"
        ''' 
        self.assertEqual(Resume.get_last_name_first_name(self.resume), 'McElhiney, Patrick')

    def test_get_experience(self):
        '''
        Tests that the Resume.get_experience(resume) is an object of model Experience
        '''
        self.assertIsNotNone(Resume.get_experience(self.resume))

    def test_get_education(self):
        '''
        Tests that the Resume.get_education(resume) is an object of model Education
        '''
        self.assertIsNotNone(Resume.get_education(self.resume))

    def test_get_qualification(self):
        '''
        Tests that the Resume.get_qualification(resume) is an object of model Qualification
        '''
        self.assertIsNotNone(Resume.get_qualification(self.resume))

    def test_get_certification(self):
        '''
        Tests that the Resume.get_certification(resume) is an object of model Certification
        '''
        self.assertIsNotNone(Resume.get_certification(self.resume))


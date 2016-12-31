from django.db import models
from django.conf import settings

class Faculty(models.Model):
    employee_id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    core_competency = models.CharField(max_length=30)
    email_id = models.EmailField(default="Invalid")
    areas_of_interest = models.TextField()
    phone_number = models.CharField(max_length=13)
    is_guide = models.BooleanField(default=False)
    allocated_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'Faculty'


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    degree_name = models.CharField(max_length=10)
    course_name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=5, default="none")

    class Meta:
        db_table = 'Course'


class Batch(models.Model):
    course = models.ForeignKey(Course, null=False)
    year = models.IntegerField(null=False)
    email_id = models.EmailField(default="Invalid")
    strength = models.IntegerField(default=0)
    tutor = models.ForeignKey(Faculty)

    class Meta:
        db_table = 'Batch'
        unique_together = ('course', 'year')


class Student(models.Model):
    SEMESTER_CHOICES = (
        (7, '7'),
        (9, '9'),
        (4, '4')
    )
    PROJECT_CATEGORY_CHOICES = (
        ('Industry', 'Industry Project'),
        ('Research', 'Institution/Research Project'),
    )
    roll_no = models.CharField(max_length=8, primary_key=True)
    course = models.ForeignKey(Course)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    name = models.CharField(max_length=100)
    email_id = models.EmailField(default="Invalid")
    phone_number = models.CharField(max_length=13)
    project_category = models.CharField(max_length=20,choices=PROJECT_CATEGORY_CHOICES,blank=True)
    organization_name = models.CharField(max_length=200,blank=True)
    postal_address = models.CharField(max_length=500,blank=True)
    address_short_url = models.CharField(max_length=200,blank=True)
    mentor_name = models.CharField(max_length=100,blank=True)
    mentor_designation = models.CharField(max_length=100,blank=True)
    mentor_email_id = models.EmailField(blank=True)
    domain_key_word = models.CharField(max_length=300,blank=True)
    project_title = models.CharField(max_length=500,blank=True)
    join_date = models.CharField(max_length=10,blank=True)

    class Meta:
        db_table = 'Student'


class VMS_Session(models.Model):
    SEM_CHOICES=(
        ('odd','odd'),
        ('even','even')
    );
    session_id = models.IntegerField(primary_key=True)
    session_year = models.IntegerField(default=0)
    session_sem = models.CharField(max_length=5,choices=SEM_CHOICES)
    is_current = models.BooleanField(default=False)
    class Meta:
        db_table = 'VMS_Session'


class Tutor(models.Model):
    session = models.ForeignKey(VMS_Session)
    faculty = models.ForeignKey(Faculty)
    course = models.ForeignKey(Course)

    class Meta:
        db_table = 'Tutor'
        unique_together = ('session', 'faculty','course')



class User(models.Model):
    user_id = models.ForeignKey(Faculty)
    user_pass = models.CharField(max_length=150)
    user_role = models.IntegerField(default=-1)

    class Meta:
        db_table = 'User'
        unique_together = ('user_id', 'user_role')


class GuideStudentMap(models.Model):
    session = models.ForeignKey(VMS_Session)
    guide = models.ForeignKey(Faculty)
    student = models.ForeignKey(Student)
    tutor = models.ForeignKey(Tutor, default="-1")

    class Meta:
        db_table = 'GuideStudentMap'
        unique_together = ('session', 'guide','student')


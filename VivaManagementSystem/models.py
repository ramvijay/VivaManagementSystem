from django.db import models

class Faculty(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    nickname = models.CharField(max_length=10)
    #employee_id = models.CharField(max_length=10)
    #core_competency = models.CharField(max_length=30)
    #email_id = models.CharField(max_length=100)
    #areas_of_interest = models.TextField()
    #phone_number = models.CharField(max_length=13)
    class Meta:
        db_table = 'Faculty'
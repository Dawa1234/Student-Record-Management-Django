from distutils.command.upload import upload
from pickle import TRUE
from django.db import models


# Create your models here.
# Studner gender
gender = (
    ('Male' , 'Male'),
    ('Female' , 'Female')
)

# Student Class
studentClass = (
    ('1' , '1'),
    ('2' , '2')
)


class Student(models.Model):
    student_id=models.AutoField(auto_created=True,primary_key=True)
    student_name=models.CharField(max_length=200 , null=True, blank=True)
    student_address=models.CharField(max_length=100 ,null=True, blank=True)
    student_gender =models.CharField(max_length=100 , choices=gender)
    student_age = models.PositiveSmallIntegerField(null=True, blank=True)
    student_email = models.EmailField(max_length=100 , null=True, blank=True)
    student_phone = models.CharField(max_length=10,null=True, blank=True )
    student_class = models.CharField(max_length=100, choices=studentClass , null=True, blank=True)
    addmission_date = models.CharField(max_length=100 , blank=True)
    student_image=models.ImageField(upload_to='images',default="default.jpg", null=True, blank=True)

    class Meta:
        db_table="student_info"

    def __str__(self):
        return self.student_name

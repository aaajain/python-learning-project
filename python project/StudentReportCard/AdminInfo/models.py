from django.db import models
from datetime import datetime

# Create your models here.
# Create your models here.
class StudentDetail(models.Model):
    StudentName=models.CharField(max_length=200)
    Course= models.CharField(max_length=200)
    PhoneNumber= models.IntegerField()
    created_at= models.DateTimeField(default=datetime.now,blank=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    password= models.CharField(max_length=200,blank=True,null=True)
    status= models.NullBooleanField(blank=True,null=True,default=None)

    class Meta:
        verbose_name_plural="StudentDetail"

class SubjectDetail(models.Model):
    StudentDetailId= models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    Java=models.IntegerField()
    CSharp=models.IntegerField()
    Angular=models.IntegerField()
    Node=models.IntegerField()
    Python=models.IntegerField()
    TotalMarks= models.IntegerField()

    class Meta:
        verbose_name_plural="SubjectDetail"
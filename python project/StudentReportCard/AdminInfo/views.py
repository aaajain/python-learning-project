from django.shortcuts import render
from django.shortcuts import render
from AdminInfo.models import StudentDetail,SubjectDetail
from django.http import HttpResponse
from django.views.generic import View
import json
from .forms import loginForm
from django.db.models import Q

#getStudentsRecords View- Checking login creadentials and diplaying students data
def getStudentsRecords(request):
    form= loginForm(request.POST)
    username= request.POST.get('username')
    password= request.POST.get('password')
    login_records = StudentDetail.objects.filter(username=username,password=password)[:1]
    login_details = list(login_records)
    url=''

    if(not login_records):
        context={
            'error': 'Invalid username or password'
        }
        url='AdminInfo/error.html'

    else:
        if(login_details[0].status):
            student_records = StudentDetail.objects.exclude(id=login_details[0].id).order_by('id')
            subject_records= SubjectDetail.objects.exclude(id=login_details[0].id).order_by('StudentDetailId')
            url= 'AdminInfo/AdminHome.html'
        
        else:
            student_records=login_details
            subject_records= SubjectDetail.objects.filter(StudentDetailId=login_details[0].id).order_by('StudentDetailId')
            url='StudentInfo/StudentHome.html'
            
        context = {
            'student_records': student_records,
            'subject_records': subject_records,
            'username': username
            }

    return render(request, url, context) 

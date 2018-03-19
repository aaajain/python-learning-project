from django.shortcuts import render,redirect
from AdminInfo.models import StudentDetail,SubjectDetail
from django.http import HttpResponse
from django.views.generic import View
import json
from .forms import loginForm
from StudentInfo.views import GenerateReportCard

#getStudentsRecords View- Checking login creadentials and diplaying students data
def getStudentsRecords(request):
    form= loginForm(request.POST)
    username= request.POST.get('username')
    password= request.POST.get('password')
    login_records = StudentDetail.objects.filter(username=username,password=password)[:1]
    login_details = list(login_records)
    url=''
    
    context={
        'username':username
    }

    if(not login_records):
        context={
            'error': 'Invalid username or password'
        }
        url='AdminInfo/error.html'

    else:
        user_id=login_details[0].id
        request.session['id']=user_id
        if(login_details[0].status):
            student_records = StudentDetail.objects.exclude(id=user_id).order_by('id')
            subject_records= SubjectDetail.objects.exclude(id=user_id).order_by('StudentDetailId')
            url= 'AdminInfo/AdminHome.html'
            context = {
            'student_records': student_records,
            'subject_records': subject_records,
            'username': username,
            'user_id':user_id
            }
        
        else:
            url='StudentInfo/StudentHome.html'

    return render(request, url,context) 


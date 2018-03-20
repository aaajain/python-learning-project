from django.shortcuts import render
from django.shortcuts import render
from AdminInfo.models import StudentDetail,SubjectDetail
from django.http import HttpResponse
from django.views.generic import View
import json
from .forms import loginForm
from django.db.models import Q
import string
import random
import datetime

from django.utils.crypto import get_random_string
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

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
def insertStudentRecords(request):
	first_name = request.POST.get('first_name')
	last_name = request.POST.get('last_name')
	course = request.POST.get('course')
	phone_number = request.POST.get('phone_number')
	created_at = datetime.datetime.now()
	username = (first_name[0] + last_name)
	print(username)
	password = id_generator(4,first_name + last_name)
	print(created_at)
	p1 = StudentDetail(Course = course, PhoneNumber=phone_number,
   	created_at = created_at, username = username, password = password,
	status = '0',FirstName = first_name, LastName = last_name)
	p1.save()
	return render() 
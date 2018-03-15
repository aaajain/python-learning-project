from django.shortcuts import render
from django.shortcuts import render
from AdminInfo.models import StudentDetail
from django.http import HttpResponse
from django.views.generic import View
import json

def getStudentsRecords(request):
    student_records = StudentDetail.objects.all()
    context = {
    'student_records': student_records
    }
    return render(request, 'AdminInfo/AdminHome.html', context)
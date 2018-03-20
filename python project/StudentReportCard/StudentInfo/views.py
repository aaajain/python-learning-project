from django.shortcuts import render,redirect
from AdminInfo.models import StudentDetail,SubjectDetail
from django.http import HttpResponse
from django.views.generic import View
import json
from AdminInfo.forms import loginForm


def GenerateReportCard(request):
    user_id= request.session['id']
    subject_records= SubjectDetail.objects.order_by('StudentDetailId')
    subject_records= list(subject_records)
    student_records = StudentDetail.objects.filter(id=user_id)
    student_records= list(student_records)
    username=student_records[0].username

    rank= 1
    user_marks= [ i.TotalMarks for i in subject_records if i.StudentDetailId.id == user_id]
    for i in subject_records:
        if i.TotalMarks> user_marks[0]:
            rank+=1

    context={
        'subject_records':subject_records,
        'student_records': student_records,
        'rank':rank,
        'username':username
    }
    
    return render(request, 'StudentInfo/StudentHome.html',context)

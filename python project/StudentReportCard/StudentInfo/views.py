from django.shortcuts import render,redirect
from AdminInfo.models import StudentDetail,SubjectDetail
from django.http import HttpResponse
from django.views.generic import View
import json
from AdminInfo.forms import loginForm
from interface import implements
import StudentReportCard.recordsInterface

class Student(implements(StudentReportCard.recordsInterface.recordsInterface)):
    
    user_id=0
    username=''

    #function for generating report card for individual student
    def GenerateReportCard(request):
        
        Student.user_id= request.session['id']
        details= Student.getStudentsRecords()
        url=details[0]
        context=details[1]
        return render(request, url,context)


    #retrieve students data for individual student
    def getStudentsRecords():
        
        subject_records= SubjectDetail.objects.order_by('StudentDetailId')
        subject_records= list(subject_records)
        student_records = StudentDetail.objects.filter(id=Student.user_id)
        student_records= list(student_records)
        Student.username=student_records[0].username

        #rank calculation
        rank= 1
        user_marks= [ i.TotalMarks for i in subject_records if i.StudentDetailId.id ==Student.user_id]
        for i in subject_records:
            if i.TotalMarks> user_marks[0]:
                rank+=1

        context={
            'subject_records':subject_records,
            'student_records': student_records,
            'rank':rank,
            'username':Student.username
        }
        
        url= 'StudentInfo/StudentHome.html'
        return url,context

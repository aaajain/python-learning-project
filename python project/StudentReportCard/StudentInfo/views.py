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
    length= len(subject_records)


    for i in range(length-1):
        for elements in range(length-i-1):
            if(subject_records[elements].TotalMarks < subject_records[elements+1].TotalMarks):
                temp= subject_records[elements]
                subject_records[elements]= subject_records[elements+1]
                subject_records[elements+1]=temp
                
    #position= [ i for i in range(len(subject_records)) if subject_records[i].StudentDetailId.id==user_id]
    #rank= position[0]+1
    rankDict={}
    x=length-1
    rankIteration=0
    while(rankIteration<=x):
        print(rankIteration)
        
        if  rankIteration != x and  subject_records[rankIteration].TotalMarks== subject_records[rankIteration+1].TotalMarks:
            rankDict[subject_records[rankIteration].StudentDetailId.id]= rankIteration+1
            rankDict[subject_records[rankIteration+1].StudentDetailId.id]= rankIteration+1
            rankIteration=rankIteration+2
        else:
            rankDict[subject_records[rankIteration].StudentDetailId.id]=rankIteration+1
            rankIteration=rankIteration+1
    rank= rankDict[user_id]
    



    context={
        'subject_records':subject_records,
        'student_records': student_records,
        'rank':rank,
        'username':username
    }
    
    return render(request, 'StudentInfo/StudentHome.html',context)

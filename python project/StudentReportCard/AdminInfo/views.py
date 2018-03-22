from django.shortcuts import render,redirect
from AdminInfo.models import StudentDetail,SubjectDetail
from django.http import HttpResponse
from django.views.generic import View
from .forms import loginForm
from interface import implements
import StudentReportCard.recordsInterface

#getStudentsRecords View- Checking login creadentials and diplaying students data
class Admin(implements(StudentReportCard.recordsInterface.recordsInterface)):
    user_id=0
    username=''
    def login(request):
        form= loginForm(request.POST)
        Admin.username= request.POST.get('username')
        password= request.POST.get('password')
        login_records = StudentDetail.objects.filter(username=Admin.username,password=password)[:1]
        login_details = list(login_records)
        url=''
        
        context={
            'username':Admin.username
        }

        if(not login_records):
            context={
                'error': 'Invalid username or password'
            }
            url='AdminInfo/error.html'

        else:
            Admin.user_id=login_details[0].id
            request.session['id']=Admin.user_id
            if(login_details[0].status):
                details=Admin.getStudentsRecords()
                url=details[0]
                context=details[1]
            else:
                url='StudentInfo/StudentHome.html'

        return render(request, url,context) 

    def getStudentsRecords():
        student_records = StudentDetail.objects.exclude(id=Admin.user_id).order_by('id')
        subject_records= SubjectDetail.objects.exclude(id=Admin.user_id).order_by('StudentDetailId')
        subject_records=list(subject_records)
        url= 'AdminInfo/AdminHome.html'
                
        length= len(subject_records)
        for i in range(length-1):
            for elements in range(length-i-1):
                if(subject_records[elements].TotalMarks < subject_records[elements+1].TotalMarks):
                    temp= subject_records[elements]
                    subject_records[elements]= subject_records[elements+1]
                    subject_records[elements+1]=temp

        rankDict={}
        x=length-1
        rankIteration=0
        while(rankIteration<=x):
                        
            if  rankIteration != x and  subject_records[rankIteration].TotalMarks== subject_records[rankIteration+1].TotalMarks:
                rankDict[subject_records[rankIteration].StudentDetailId.id]= rankIteration+1
                rankDict[subject_records[rankIteration+1].StudentDetailId.id]= rankIteration+1
                rankIteration=rankIteration+2
            else:
                rankDict[subject_records[rankIteration].StudentDetailId.id]=rankIteration+1
                rankIteration=rankIteration+1
                
        college= SingleToneCollege.__new__(SingleToneCollege,'MET', 'Bandra', 'Mumbai University')
        
        collegeDetails=college.collegeName, college.collgeAddr, college.collegeBoard
        context = {
            'student_records': student_records,
            'subject_records': subject_records,
            'username': Admin.username,
            'user_id':Admin.user_id,
            'college':collegeDetails,
            'rank':rankDict 

            }

        return url,context 


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



# Singleton/ClassVariableSingleton.py
class SingleToneCollege(object):
    __instance = None
    def __new__(cls, collegeName, collgeAddr, collegeBoard ):
        if SingleToneCollege.__instance is None:
            SingleToneCollege.__instance = object.__new__(cls)
            SingleToneCollege.__instance.collegeName = collegeName
            SingleToneCollege.__instance.collgeAddr= collgeAddr
            SingleToneCollege.__instance.collegeBoard= collegeBoard
        return SingleToneCollege.__instance 



from django.shortcuts import render,redirect
from AdminInfo.models import StudentDetail,SubjectDetail
from django.http import HttpResponse
from django.views.generic import View
from .forms import loginForm
from interface import implements
import StudentReportCard.recordsInterface
from django.template.context_processors import request
from django.template import response
from xlrd import open_workbook
from django.db.models import Avg
import subprocess
import os
import clr
import ClassLibrary1

import datetime
import xlsxwriter
import json

#getStudentsRecords View- Checking login creadentials and diplaying students data
class Admin(implements(StudentReportCard.recordsInterface.recordsInterface)):
    user_id=0
    username=''
    def chkavg(request):
        subjectname=request.POST.get('subname')
        marks=  SubjectDetail.objects.all().aggregate(Avg(subjectname))
        subprocess.call(['java','-jar','c:\\amahajan-0.0.1-SNAPSHOT.jar'])
        
#         clr.AddReference("c:\\abc\\ClassLibrary1.dll")
#         frm=ClassLibrary1.Class1()
#         val=frm.printMessage()
#         print(val)
#             
      
#         pre = os.path.dirname(os.path.realpath(__file__))
#         fname = 'ClassLibrary1.dll'
#         clr.AddReference("fname")
#         path = os.path.join(pre, fname) 
        print(marks)
        context = {
            'SubjectName': subjectname,
            'AverageMarks': marks
           
        }
        url='AdminInfo/mypage.html'
        return render(request, url,context)
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
            list1=['Java','CSharp','Angular','Node','Python'] 
        data = StudentDetail.objects.filter(id=1).values()
            
        print(data[0]['id'])
        pre = os.path.dirname(os.path.realpath(__file__))
        fname = 'demo.xlsx'
        path = os.path.join(pre, fname)        
        workbook = xlsxwriter.Workbook(path)
        wb = workbook.add_worksheet()
        wb.write('A1',data[0]['id'])
        wb.write('B1',data[0]['Course'])
        wb.write('C1',data[0]['PhoneNumber'])
        wb.write('D1',data[0]['username'])
        wb.write('E1',data[0]['password'])
        wb.write('F1',data[0]['status'])
        wb.write('G1',data[0]['FirstName'])
        wb.write('G1',data[0]['LastName'])
        workbook.close()
        

        college= SingleToneCollege.__new__(SingleToneCollege,'MET', 'Bandra', 'Mumbai University')
        
        collegeDetails=college.collegeName, college.collgeAddr, college.collegeBoard

        context = {
            'student_records': student_records,
            'subject_records': subject_records,
            'username': Admin.username,
            'user_id':Admin.user_id,
            'college':collegeDetails,
            'rank':rankDict, 
			'subjects':list1		
            }

        return url,context 

    def excelInsert(request):
        pre = os.path.dirname(os.path.realpath(__file__))
        fname = 'StudentData.xlsx'
        path = os.path.join(pre, fname)
        wb = open_workbook(path)
        # Reading Data from the excel sheet
        values = list()
        data = list()
        for s in wb.sheets():
            number_row = s.nrows
            number_col = s.ncols
            for row in range(1,number_row):
                 
                for col in range(number_col):
                    value  = (s.cell(row,col).value)
                    try:
                        value = str(int(value))
                    except ValueError:
                        pass
                    finally:
                        values.append(value)        
                data.append(values)
                values = []      
        saveObj = StudentDetail(id = data[0][0],Course = data[0][1], PhoneNumber=data[0][2],
                created_at = datetime.datetime.now(), FirstName = data[0][4], LastName = data[0][5],
                password = data[0][6], status = '0',username = data[0][8])
        saveObj.save()               
#         for x in range(len(data)):
#             for y in data[x]:
#                 print(y)
#                 
#                 saveObj = StudentDetail(id = data[x][y],Course = data[x][y], PhoneNumber=data[x][y],
#                 created_at = datetime.datetime.now(), username = data[x][y], password = data[x][y],
#                 status = '0',FirstName = data[x][y], LastName = data[x][y])
#                 saveObj.save()
        return render(request, 'AdminInfo/NewRecord.html')

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



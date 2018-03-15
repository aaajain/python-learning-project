from django.shortcuts import render
from AdminInfo.models import StudentDetail
from django.http import HttpResponse
import json
#from django.http import JsonResponse
#from serpy import Serializer, IntField, StrField, MethodField
from django.views.generic import View
def getStudentsRecords(request):
	student_records= StudentDetail.objects.all().values()
	#student_list = list(student_records)
	#context = {'key':student_records}
	render(request,'AdminInfo/AdminHome.html',student_records)
	#print('bcjsabncdkjq')
	#print(student_list)
	#print(JsonResponse(student_list,safe=False))
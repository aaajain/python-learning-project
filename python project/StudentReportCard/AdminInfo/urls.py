from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'AdminHome/', TemplateView.as_view(template_name="AdminInfo/AdminHome.html"), name="AdminHome"),
    url(r'^getStudentsRecords/$',views.getStudentsRecords, name='getStudentsRecords'),
    url(r'^insertStudent/$',views.insertStudentRecords, name='insertStudentRecords')
    #url(r'^insertStudent/(?P<first_name>\w+)/(?P<last_name>\w+)/(?P<course>\w+)/(?P<phone_number>\d+)/$',views.insertStudentRecords, name='insertStudentRecords')
]

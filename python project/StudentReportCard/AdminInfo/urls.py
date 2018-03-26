from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'AdminHome/', TemplateView.as_view(template_name="AdminInfo/AdminHome.html"), name="AdminHome"),
    url(r'^login/$',views.Admin.login, name='login'),
       url(r'^checkavergage/$',views.Admin.chkavg, name='chkavg'),
       url(r'^excelInsert/$',views.Admin.excelInsert, name='excelInsert'),
    	url(r'^insertStudent/$',views.insertStudentRecords, name='insertStudentRecords')
    #url(r'^bubbleSort/$',views.bubbleSort, name='bubbleSort')

]
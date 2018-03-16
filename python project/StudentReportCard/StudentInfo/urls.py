from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'StudentHome/', TemplateView.as_view(template_name="StudentInfo/StudentHome.html"), name="StudentHome"),
    #url(r'^getStudentsRecords/$',views.getStudentsRecords, name='getStudentsRecords')

]

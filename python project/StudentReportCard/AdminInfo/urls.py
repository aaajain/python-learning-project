from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'AdminHome/', TemplateView.as_view(template_name="AdminInfo/AdminHome.html"), name="AdminHome"),
    url(r'^getStudentsRecords/$',views.getStudentsRecords, name='getStudentsRecords'),
    #url(r'^bubbleSort/$',views.bubbleSort, name='bubbleSort')

]

from django.conf.urls import url
from StudentInfo.views import Student
from django.views.generic import TemplateView


urlpatterns = [
    url(r'StudentHome/', TemplateView.as_view(template_name="StudentInfo/StudentHome.html"), name="StudentHome"),
    url(r'^GenerateReportCard/$',Student.GenerateReportCard, name='GenerateReportCard'),

]

"""
WSGI config for StudentReportCard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from AdminInfo.views import SingleToneCollege
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudentReportCard.settings")

application = get_wsgi_application()

global college
college= SingleToneCollege.__new__(SingleToneCollege,'MET','Bandra','Mumbai University') 

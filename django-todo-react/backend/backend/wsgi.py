"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys 
from django.core.wsgi import get_wsgi_application
#sys.path.append(') 
# adjust the Python version in the line below as needed 
#sys.path.append('/var/www/vhosts/mysite/venv/lib/python3.5/site-packages') 
#sos_environment['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
 

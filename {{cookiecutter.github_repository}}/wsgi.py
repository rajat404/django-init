# -*- coding: utf-8 -*-
"""WSGI config for  project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.
"""

# Standard Library
import os

# Third Party Stuff
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv


# Read .env file and set key/value inside it as environement variables
# see: http://github.com/theskumar/python-dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

"""
WSGI config for maru_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
from unipath import Path

# EDIT THIS VALUE
VIRTUAL_PATH = ''
# VIRTUAL_PATH='/home/isatsiuk/PycharmProjects/BK001/.env'

if VIRTUAL_PATH != '':
    activate_this = '{}/bin/activate_this.py'.format(VIRTUAL_PATH)
    execfile(activate_this, dict(__file__=activate_this))


BASE_DIR = Path(os.path.abspath(__file__)).ancestor(2)

sys.path.insert(0, BASE_DIR)
# sys.path.insert(0, BASE_DIR.child("lib"))
# sys.path.insert(0, '/home/isatsiuk/PycharmProjects/BK001/Booktype/lib/')

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use

os.environ["DJANGO_SETTINGS_MODULE"] = "maru_blog.settings"
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mybook_site.settings.dev")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "maru_blog.settings")


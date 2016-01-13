import sys
from django.conf import settings
from django.conf.urls import patterns

settings.configure(
    STATIC_URL='/',
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'middleware.RequireCurrentUser',
    ),
    TEMPLATE_DIRS=('./templates',),
    STATICFILES_DIRS=('./static',),
)

from views import *

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

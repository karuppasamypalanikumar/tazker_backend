import os
from tazker.settings.base import *
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# settings_dev.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": 'tazker',
        "USER": 'karuppasamypalanikumar',
        "PASSWORD": '',
        "HOST": "localhost",
        "PORT": 5432,
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
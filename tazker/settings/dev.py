import os
from tazker.settings.base import *
from dotenv import load_dotenv
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

load_dotenv()

# settings_dev.py
if os.environ.get('DB') == "POSTGRES":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            "NAME": 'tazker',
            "USER": 'karuppasamypalanikumar',
            "PASSWORD": '',
            "HOST": "localhost",
            "PORT": 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'tazker.sqlite3'
        }
    }

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
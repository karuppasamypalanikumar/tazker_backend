import os
from tazker.settings.base import *
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# settings_dev.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
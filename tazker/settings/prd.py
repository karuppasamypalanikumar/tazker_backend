from tazker.settings.base import *
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": 'postgres',
        "USER": 'postgres',
        "PASSWORD": 'Karuppasamy22',
        "HOST": "tazker-dev-new.cauiydqtyks7.eu-north-1.rds.amazonaws.com",
        "PORT": 5432,
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
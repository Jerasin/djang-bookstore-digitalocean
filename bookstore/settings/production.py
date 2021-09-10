from .base import *  # Import base settings from settings/__init__.py

from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG_PRO')

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-gx%xf5_w)ldyq$_%a@-@xj9=7!+ep0@f$+^sa*bc)2x%6&=9=*'
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = [
                '188.166.208.101',
                '127.0.0.1'
                ]

DATABASES = {
    'default': {     
    'ENGINE': 'django.db.backends.postgresql_psycopg2',       
    'NAME': 'bookstore',       
    'USER': 'djangouser',        
    'PASSWORD': 'Jc@12345678',        
    'HOST': 'localhost',       
    'PORT': '',    
    }
}

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file"]},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": '/bookstore/logs/bookstore.log',
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True
        },
    },
    "formatters": {
        "app": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}





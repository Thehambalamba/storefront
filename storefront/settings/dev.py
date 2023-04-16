from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-nwtfvs%c)q!xw6#_#(obi+19ah(@qdbw&ac^nrkw56abf39j5@'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
    }
}

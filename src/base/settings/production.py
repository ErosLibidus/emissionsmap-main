from .base import *

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')
ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME' : os.getenv('NAME'),
	    'USER' : os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
	    'HOST' : os.geten('HOST'),
	    'PORT': '5432',
    }
}
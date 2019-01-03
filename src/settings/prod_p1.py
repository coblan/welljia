from .prod import *

DATABASES = {
    'default': {
        'NAME': 'welljia_p1',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root123456789',
        'HOST': '127.0.0.1', 
        'PORT': '3306',        
      },
    }
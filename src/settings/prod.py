from .base import *


DATABASES = {
    'default': {
        'NAME': 'welljia',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root123456789',
        'HOST': '127.0.0.1', 
        'PORT': '3306',        
      },
    }


#TENCENT = {
    #'SdkAppId': '1400091635',
    #'AppKey': '3d5e973b84eb1d76a3b92c05bdbbdc85',
#}

TENCENT = {
    'SdkAppId': '1400144729',
    'AppKey': '1a8093135b4e91df3b7d76535437a98f',
    'validate_temp': '199823',
}

ALLOWED_HOSTS = ['*']

SELF_URL = 'http://www.vr-home.com.cn'
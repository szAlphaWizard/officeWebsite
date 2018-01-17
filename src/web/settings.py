import os
from conf import app_conf

APPEND_SLASH = True
DEBUG = True

ROOT_URLCONF = 'web.urls'
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    "django_extensions",
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(app_conf.CONF['app_home'], 'var/app.db'),
    }

}

SECRET_KEY = 'jmws_8td@h11eu_zn1+__n=ukqb415890tzn0n=c6_dhr23%=!^1s1pzsc5bp'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = True
SESSION_COOKIE_AGE = 3600 * 72


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(app_conf.CONF['app_home'], "src/web/templates")],
        'OPTIONS':{
            'context_processors': [
                'django.template.context_processors.request',
            ],
        }
    },
]
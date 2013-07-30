# -*- coding:utf-8 -*-
import settings


ALLOWED_HOSTS = ["*"]

# #from service_catalog.settings import *
# #from conf.settings import *
#
# ADMIN_TOOLS_MENU = 'service_catalog.menu.CustomMenu'
# ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'service_catalog.dashboard.CustomAppIndexDashboard'

DEBUG = True
#DEBUG = False

TIME_ZONE = 'Europe/Madrid'


DEFAULT_FROM_EMAIL = 'gilcu2@gmail.com'
EMAIL_FROM = 'gilcu2@gmail.com'
EMAIL_HOST_USER = "gilcu2@gmail.com"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_PASSWORD = "es35ther"
EMAIL_PORT=587
EMAIL_USE_TLS = True
EMAIL_DEBUG=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'counts',
        'USER': 'root',
        'PASSWORD': 'mysql35root',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

#
#
# settings.USE_DJANGO_SERVE = True
#
# DEFAULT_DOMAIN = "57.anvil.com"
#
# BROKER_URL =""
# BROKER_HOST = "127.0.0.1"
# BROKER_PORT = 5672
# BROKER_VHOST = "/my_vhost"
# BROKER_USER = "my_rabbit_user"
# BROKER_PASSWORD = "1234"
# CELERY_RESULT_BACKEND = "amqp"

# To test https
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_HTTPONLY = True




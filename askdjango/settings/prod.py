from .common import *

DEBUG = False

INSTALLED_APPS += ['storages']

import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DB_NAME'],
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}

STATICFILES_STORAGE = 'askdjango.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'askdjango.storages.MediaS3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = 'askdjango-allieus'
AWS_S3_REGION_NAME = 'ap-northeast-2'

ALLOWED_HOSTS = ['*']


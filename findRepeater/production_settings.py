import dj_database_url
from .settings import *


DEBUG = False

TEMPLATE_DEBUG = False

SECRET_KEY = 'sy5d2#$j3zbxq*@dgm60--&_3=ie($$$jc=3tdqs=2739^!yqe'

ALLOWED_HOSTS = ['findrep.herokuapp.com']

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '#XoOOpsPAsdfqZxqswcq^)(k=)8zzCWBVWEjoij2113#2101_w3izo)$u&&&zsz%p)rbhu3w'
DEBUG = True
ALLOWED_HOSTS = ['46.101.218.78', 'mamapapas.club']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mamapapas_db',
        'USER': 'mamapapas_db_user',
        'PASSWORD': 'k3Nf3bnEir45bye',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static/') 
# ]

STATIC_URL = '/static/'
STATIC_ROOT = '/home/chef/mamapapas/mamapapas/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/chef/mamapapas/mamapapas/media/'

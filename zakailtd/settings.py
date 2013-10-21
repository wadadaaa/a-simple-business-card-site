# Django settings for zakailtd project.


import os
import sys
import os.path
#import dj_database_url
#import djcelery
#import s3utils
# settings.py
'''

def map_path(directory_name):
    return os.path.join(os.path.dirname(__file__),
        '../' + directory_name).replace('\\', '/')


TEMPLATE_DIRS = (
    map_path('templates'),
)
'''
#AWS_ACCESS_KEY_ID = os.environ.get('AKIAIXCBEASBXJEJ6OZQ')
#AWS_SECRET_ACCESS_KEY = os.environ.get('D8R+zxA5kTedAtBMdEzRBBGkJZRu9jCrAtNykWWf')
#AWS_STORAGE_BUCKET_NAME = '<forheroku>'

#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

#STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
# = STATIC_URL + 'admin/'

#djcelery.setup_loader()
#CELERY_ALWAYS_EAGER = True
#CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
#DEFAULT_FILE_STORAGE = 's3utils.MediaRootS3BotoStorage'
#STATICFILES_STORAGE = 's3utils.StaticRootS3BotoStorage'

#CELERY_RESULT_BACKEND = "database"
#CELERY_RESULT_DBURI = "sqlite:///mydatabase.db"


#DATABASES = {
#    'default': dj_database_url.config()
#}
PROJECT_DIR = os.path.dirname((os.path.dirname((os.path.dirname(__file__)))))

#PROJECT_ROOT = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__))))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Anna Lopatinski', 'lopatinski@gmail.com'),
)

MANAGERS = ADMINS



#DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
#DATABASE_NAME = 'ddnp15jj5vfu94'
#DATABASE_USER = 'akbhnlvclallia'
#DATABASE_PASSWORD = 'cqJ7rodjDt3mNQoR4w9aK8lYCi'
#DATABASE_HOST = 'ec2-54-235-155-40.compute-1.amazonaws.com'
#DATABASE_PORT = '5432'




# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static_export')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),

    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8pld)4=jvx_586&amp;=qh3^#i&amp;wy_(+6l9f0g4_5dno&amp;r06ko^uf7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zakailtd.urls'

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'zakailtd.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR,'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'mptt',
    'zakai',
    'easy_thumbnails',
    #'storages',
    #'queued_storage',
    #'djcelery',
    #'django.contrib.sitemaps',
)
WHOOSH_INDEX = os.path.join(PROJECT_DIR, 'whoosh/')



THUMBNAIL_ALIASES = {
    '': {
        'small': {'size' : (150, 150), 'crop': 'smart'},
        'large': {'size' : (400, 400), 'crop': 'smart'},


        }
}
try:
    from .local_settings import *
except ImportError:
    pass






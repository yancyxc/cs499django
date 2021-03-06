import os.path
import os
import dj_database_url

# Django settings for cs499 project.

# The absolute path to the project's root.
PROJ_ROOT = os.path.dirname(os.path.realpath(__file__))

# This sets path to be specific for your computer
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# Debugging and dev options
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Needed for email
DEFAULT_FROM_EMAIL = 'h.shiner3802@gmail.com'
SERVER_EMAIL = 'h.shiner3802@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'h.shiner3802@gmail.com'
EMAIL_HOST_PASSWORD = 'zaring123'
EMAIL_PORT = 587

CLIENT_ID = '51f47d45fe00457294c9f14331c2d7f22222'
CLIENT_SECRET = 'a3f8402dfb903dae6f176f51e41454f42222'
# lvh.me is just a domain name for localhost
REDIRECT_URI = 'http://127.0.0.1:8000/authorize/callback'


AUTH_PROFILE_MODULE = "UserProfile"

# Admins and their email addresses
ADMINS = (
<<<<<<< HEAD
    
=======
    # ('Hillary Shiner', 'hashin2@g.uky.edu'),
>>>>>>> 11315b61f739cbec77d8c1b402ba235432d88cb4
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'database',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': 'password',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Louisville'

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
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(PROJ_ROOT, 'cs499/cs499_app/views/static_files')

    PROJECT_PATH + '/static/css',
    PROJECT_PATH + '/static/image',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'n)!ckm9*tz)l_yihrdw4z(pux0ns*zf6g=(@otm%m&amp;zsqrc*cv'

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
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cs499.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'cs499.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
<<<<<<< HEAD
    os.path.join(PROJ_ROOT, 'templates'),    
=======
    os.path.join(PROJ_ROOT, 'templates'),
    'C:/Users/Hillary/Documents/Spring13/CS499/cs499-django/cs499/cs499_app/registration'
>>>>>>> 11315b61f739cbec77d8c1b402ba235432d88cb4
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'django_extensions',
    'cs499.cs499_app',
    'django.contrib.admin',   
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
<<<<<<< HEAD
=======
    # 'cs499.cs499_app.registration',
>>>>>>> 11315b61f739cbec77d8c1b402ba235432d88cb4
    'registration',

)

# AUTH_PROFILE_MODULE = "registration.accounts.userprofile"
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/session/"
LOGOUT_REDIRECT_URL = "/accounts/logout/"

ACCOUNT_ACTIVATION_DAYS = 4 #Four day activation window

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'filters': {
#        'require_debug_false': {
#            '()': 'django.utils.log.RequireDebugFalse'
#        }
#    },
#    'handlers': {
#   },
#    'loggers': {
#        'django.request': {
#            'handlers': ['mail_admins'],
#            'level': 'ERROR',
#            'propagate': True,
#        },
#    }
# }        'mail_admins': {
#            'level': 'ERROR',
#            'filters': ['require_debug_false'],
#            'class': 'django.utils.log.AdminEmailHandler'
#        }


# CS499 App settings
# How many users to include in the leaderboard.
LEADERBOARD_CUTOFF = 50

# Override stuff with the settings_local.py file (or settings_heroku.py if
# we're on heorku
heroku_db = dj_database_url.config()
if heroku_db:
    print 'Using heroku settings'
    from settings_heroku import *
else:
    print 'Using local settings'
    from settings_local import *


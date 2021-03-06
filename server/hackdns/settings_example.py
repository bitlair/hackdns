# Django settings for hackdns project.

import os

HACKDNS_ROOT = os.path.dirname(os.path.abspath(__file__))
HACKDNS_HTML = os.path.join(HACKDNS_ROOT, 'templates')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
        'OPTIONS': {
#            'init_command': "PRAGMA key='secret'",
        },
    }
}

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
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1hr(8+hsqt_=ql^!8m_7l1js@j@+*#8@s42u%!#ugh#u)$p5-2'

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
    'hackdns.security.ServerSecurityMiddleware',
)

ROOT_URLCONF = 'hackdns.urls'

TEMPLATE_DIRS = (
    HACKDNS_HTML,
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'hackdns.root',
    'hackdns.entity',
)

# Server crypto
HACKDNS_RSA_EXPONENT = 65537
HACKDNS_KEY_PRIVATE  = os.path.join(HACKDNS_ROOT, 'secure', 'server.key')
HACKDNS_KEY_PRIVATE  = os.path.join(HACKDNS_ROOT, 'secure', 'server.pub')
# Server fqdn
HACKDNS_SERVER_FQDN  = 'test.root.hack'
HACKDNS_SERVER_TEST  = 'test.root.hack'
# SERVER_PORT: Use 80 for production
# SERVER_PORT: Use 8042 to talk to the development server
HACKDNS_SERVER_PORT  = 80
# Default queue life time
HACKDNS_QUEUE_TTL    = 300

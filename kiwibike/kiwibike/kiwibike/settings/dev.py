from .base import *  # noqa

INSTALLED_APPS += ['drf_yasg', 'silk']  # noqa

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += ('rest_framework.authentication.SessionAuthentication',)  # noqa

JWT_AUTH = {
    'JWT_VERIFY_EXPIRATION': False, }

MIDDLEWARE += ['silk.middleware.SilkyMiddleware'] # noqa


ALLOWED_HOSTS += ["kiwibike-be.dev.thinkeasy.cz"]  # noqa


CORS_ORIGIN_ALLOW_ALL = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',  # change debug level as appropiate
            'propagate': False,
        },
        'qinspect': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (  # noqa
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
        )

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MEDIA_ROOT = '/media'
MEDIA_URL = '/files/'

from .base import *  # noqa

INSTALLED_APPS += ['drf_yasg', 'silk']  # noqa

JWT_AUTH = {
    'JWT_VERIFY_EXPIRATION': False,
}

MIDDLEWARE += ['silk.middleware.SilkyMiddleware'] # noqa

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += ('rest_framework.authentication.SessionAuthentication',)  # noqa

LANGUAGE_CODE = 'en'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

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
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer'
        )

MEDIA_ROOT = '/tmp'
MEDIA_URL = '/files/'

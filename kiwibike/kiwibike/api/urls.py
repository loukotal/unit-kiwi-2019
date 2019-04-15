from django.urls import path, include  # noqa

from django.conf import settings

urlpatterns = [
    path("bike/", include("bikesharing.urls")),
]

if settings.DEBUG:
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="kiwibike Backend API",
            default_version='v1',
            ),
        validators=['flex'],
        public=True)

    urlpatterns += [path('docs/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui')]

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    # Esquema OpenAPI en JSON
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # # Swagger UI ejemplo de documentación
    # path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # # Redoc
    # path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # API real
    #  path('api/', include('mi_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

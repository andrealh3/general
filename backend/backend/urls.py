from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('nombreapp/', include('nombreapp.urls')), # nombreapp de tu aplicación Django
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('', RedirectView.as_view(url='nombreapp/', permanent=False)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
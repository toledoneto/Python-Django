from django.contrib import admin
from django.urls import path, include
from clients import urls as clients_urls
from home import urls as home_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include(home_urls)),
    path('clients/', include(clients_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'), # Importa view de login do Django
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

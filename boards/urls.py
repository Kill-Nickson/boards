from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('users.urls')),
    path('accounts/', include('allauth.urls')),

    # Local apps
    path('', include('pages.urls')),
    path('blackboards/', include('blackboards.urls')),
]


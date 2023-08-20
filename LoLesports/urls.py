from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # players
    path('api/v1/players/', include('apps.players.urls')),
    # teams
    path('api/v1/teams/', include('apps.teams.urls')),
    # events
    path('api/v1/events/', include('apps.competitives.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

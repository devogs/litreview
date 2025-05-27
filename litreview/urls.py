# litreview/urls.py

from django.contrib import admin
from django.urls import path, include # Import include
from django.conf import settings # Add this line for static/media in development
from django.conf.urls.static import static # Add this line for static/media in development

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')), # Include your reviews app URLs
    path('accounts/', include('accounts.urls')), # Assuming you have an accounts app with its own urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
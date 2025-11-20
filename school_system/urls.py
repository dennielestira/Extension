# school_system/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts.views import home2  # Import the home view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),# Make sure to include the accounts app URLs
    path('', home2, name='home2'),  # This will redirect the root URL to the home page
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
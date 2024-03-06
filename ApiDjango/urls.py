# En APIDjango/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Api/', include('Api.urls')),  # Aquí incluyes las rutas de tu aplicación 'api'
    # Otras rutas de tu aplicación principal
]

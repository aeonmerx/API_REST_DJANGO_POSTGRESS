# En api/urls.py
from django.urls import path
from .views import animal_list, animal_detail, planta_list, planta_detail, vehiculo_list, vehiculo_detail

urlpatterns = [
    path('animales/', animal_list, name='animal-list'),
    path('animales/<int:pk>/', animal_detail, name='animal-detail'),
    path('plantas/', planta_list, name='planta-list'),
    path('plantas/<int:pk>/', planta_detail, name='planta-detail'),
    path('vehiculos/', vehiculo_list, name='vehiculo-list'),
    path('vehiculos/<int:pk>/', vehiculo_detail, name='vehiculo-detail'),
    # Otras rutas según sea necesario
]

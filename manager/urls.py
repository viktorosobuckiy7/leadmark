from django.contrib import admin
from django.urls import path, include
from .views import manager, reservations_list, update_reservation

app_name = 'manager'


urlpatterns = [
    path('', manager),
    path('reservations/', reservations_list, name='reservations_list'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reserve')
]
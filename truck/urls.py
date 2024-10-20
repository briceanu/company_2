from django.urls import path
from .views import Create_Truck, List_Truck



urlpatterns = [
    path('create',Create_Truck.as_view(),name='create_truck'),
    path('list',List_Truck.as_view(),name='list_trucks')

    ]
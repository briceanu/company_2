from django.urls import path
from .views import SaveShift,ListTotalHours,WorkingDrivers,WeightDistanceView, TotalPayment



urlpatterns = [
    path('shift',SaveShift.as_view(),name='save_shift'),
    path('list_total_hours',ListTotalHours.as_view(),name='total_hours'),
    path('hard_working',WorkingDrivers.as_view(),name='hard_working'),
    path('weight',WeightDistanceView.as_view(),name='weigth_distance'),
    path('total_payment',TotalPayment.as_view(),name='total_payment')
    ]
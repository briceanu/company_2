from django.urls import path
from .views import SaveShift,ListTotalHours,WorkingDrivers,WeightDistanceView, TotalPayment,TotalHoursWorkedByDriver
from .views import Payment,LongestDistance,NumberOfDrivers, HoursWorked,Bonus
 

urlpatterns = [
    path('shift',SaveShift.as_view(),name='save_shift'),
    path('list_total_hours',ListTotalHours.as_view(),name='total_hours'),
    path('hard_working',WorkingDrivers.as_view(),name='hard_working'),
    path('weight',WeightDistanceView.as_view(),name='weigth_distance'),
    path('total_payment',TotalPayment.as_view(),name='total_payment'),
    path('total_hours',TotalHoursWorkedByDriver.as_view(),name='total_hours'),
    path('payment',Payment.as_view(),name='payment'),
    path('longest',LongestDistance.as_view(),name='longest'),
    path('nr_drivers',NumberOfDrivers.as_view(),name='nr_drivers'),
    path('hours_worked',HoursWorked.as_view(),name='hours_worked'),
    path('bonus',Bonus.as_view(),name='bonus')
    ]
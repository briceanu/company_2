
from django.urls import path
from .views import Sign_up, List_Drivers,Remove_driver,Update_password
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

# TokenObtainPairView ==> obtain access and refreshtokens
# TokenRefreshView   ===> provide refresh and get back accesstoken

urlpatterns = [
    path('sign_up',Sign_up.as_view({'post':'create'}),name='create_driver'),
    path('sign_in',TokenObtainPairView.as_view(),name='sign_in'),
    path('new_access_token',TokenRefreshView.as_view(),name='new_access_token'),
    path('list',List_Drivers.as_view({'get':'list'}),name='list_drivers'),
    path('remove_driver',Remove_driver.as_view({'delete':'destroy'}),name='remove_driver'),
    path('sign_out',TokenBlacklistView.as_view(),name='sign_out'),
    path('update_password',Update_password.as_view(),name='update_password')
    
]

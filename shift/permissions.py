from rest_framework.permissions import BasePermission
from driver.models import Driver

class IsAuthenticatedAndUser(BasePermission):
    def has_permission(self, request, view):
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # For POST requests (shift creation), ensure the authenticated user is the driver
        if request.method == 'POST':
            driver_id = request.data.get('driver_id')  # Ensure this is the correct key
            
            # Check if the driver exists and compare the request.user with the driver.username
            try:
                driver = Driver.objects.get(driver_id=driver_id)  # Match by the primary key
                return request.user.username == driver.username  # Compare the authenticated user's username with the driver.username
            except Driver.DoesNotExist:
                return False
        
        return True

    def has_object_permission(self, request, view, obj):
        # Ensure that only the owner of the shift can edit/delete/view it
        return request.user.username == obj.driver_id.username  # Assuming 'driver_id' is a ForeignKey to Driver


class IsAuthAndOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.driver_id == obj.driver_id

 
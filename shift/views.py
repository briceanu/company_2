from .models import Shift
from .serializers import ShiftSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import CreateModelMixin ,ListModelMixin , RetrieveModelMixin 
from .permissions import IsAuthenticatedAndUser,IsAuthAndOwner
from django.db.models import F , Q 
from django.db.models import Sum, Avg, Count, Max, Min
from rest_framework.exceptions import NotFound
from driver.models import Driver
from decimal import Decimal



class SaveShift(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [IsAuthenticatedAndUser]
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class ListTotalHours(GenericAPIView,ListModelMixin):

    def get(self,request,*args,**kwargs):
        try:
            total_hours = Shift.objects.aggregate(total_work=Sum('hours_worked'))
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(total_hours)


    # hours_worked   distance_driven

class WorkingDrivers(GenericAPIView,ListModelMixin):
    def get(self,request,*args,**kwargs):
        hours= request.data.get('hours')
        distance = request.data.get('distance')
        if not hours or not distance:
            return Response({'error':'no distance or hours'},status=status.HTTP_400_BAD_REQUEST)
        try:
            hard_working = Shift.objects.filter(
                Q(hours_worked__gte=hours) & Q(distance_driven__gte=distance)
            )
        except Exception as e: 
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if not hard_working.exists():
            return Response({'message': 'No shifts found matching the criteria.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ShiftSerializer(hard_working, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    



class WeightDistanceView(GenericAPIView,ListModelMixin):
    # weigth_carried    distance_driven
    def get(self,request,*args,**kwargs):
        try:
            weight_plus_distance = Shift.objects.aggregate(
                weight_and_distance=Sum(F('weight_carried') + F('distance_driven')))
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(weight_plus_distance)
    


    # hourse_worked    # payment_per_hour

class TotalPayment(GenericAPIView):
    permission_classes = [IsAuthAndOwner]

    def get(self, request, *args, **kwargs):
        owner = self.request.user.driver_id
        payment_per_hour = request.data.get('payment_per_hour')

        if not payment_per_hour:
            return Response({'error': 'Payment per hour is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            owner_shifts = Shift.objects.filter(driver_id=owner)
        except Shift.DoesNotExist:
            raise NotFound(detail=f'No shifts found for owner with driver ID {owner}.')
        try:
            driver = Driver.objects.get(driver_id=owner)
        except Driver.DoesNotExist:
            raise NotFound(detail=f'No driver with the driver_id {owner} found.')
        self.check_object_permissions(request, driver)
        
        payment = owner_shifts.aggregate(total_hours=Sum(F('hours_worked')))['total_hours']
        total_payment = Decimal(payment) * Decimal(payment_per_hour) if payment else 0


        return Response({'total_payment': total_payment}, status=status.HTTP_200_OK)

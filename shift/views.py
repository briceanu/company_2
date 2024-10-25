from .models import Shift
from .serializers import ShiftSerializer,HoursWorkedSerializer,BonusSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import CreateModelMixin ,ListModelMixin  
from .permissions import IsAuthenticatedAndUser,IsAuthAndOwner
from django.db.models import Q, F, Sum, Avg, Count, Max, Min
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




class TotalHoursWorkedByDriver(GenericAPIView):
    def get(self, request, *args, **kwargs):
        shifts = Shift.objects.values('driver_id').annotate(total_hours=Sum('hours_worked'))
        # annotate() method is used to add an aggregate value to each dictionary returned by values().
        if not shifts:
            raise NotFound(detail='No shifts found')

        data = []
        for shift in shifts:
            data.append({
                'driver_id': shift['driver_id'],  
                'total_hours': shift['total_hours'] or 0,  
            })
        return Response(data, status=status.HTTP_200_OK)



class Payment(GenericAPIView):
    permission_classes=[IsAuthAndOwner]
    def get(self,request):
        # list  all the shifts that belong to a single driver
        driver_id = self.request.user.driver_id
        if not driver_id:
            raise NotFound(detail='no driver_id found in the request')        

        shifts_owned_by_driver=Shift.objects.filter(driver_id=driver_id)
        # print(shifts_owned_by_driver[3].distance_driven)
        if shifts_owned_by_driver is None:
            raise NotFound(detail=f'the driver with id {driver_id} has no shifts')
        # hours_worked payment_per_hour
        try:
            """
            # we take all the shifts that belong to the driver and add a new field called hours_multi_payment
            for each shift
            """
            shifts = shifts_owned_by_driver.annotate(hours_multi_payment=F('hours_worked') * F('payment_per_hour'))
            print(shifts)
            """
            then we add the sum of these field
            """
            total_payment = shifts.aggregate(total_sum=Sum('hours_multi_payment'))
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

        data = {'payment':total_payment['total_sum']}


        return Response(data,status=status.HTTP_200_OK)
    


class LongestDistance(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:
            # find the maximum distance driven by a driver
            distance = Shift.objects.aggregate(longest_distance=Max('distance_driven'))
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if distance is None:
            return Response({'message': 'No distance data available.'}, status=status.HTTP_404_NOT_FOUND)
                
        data = {'longest_distance':distance['longest_distance']}
        return Response(data,status=status.HTTP_200_OK)


        
class NumberOfDrivers(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:
            # find the number of drivers
            drivers = Shift.objects.aggregate(nr_of_drivers=Count('driver_id',distinct=True))
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if drivers['nr_of_drivers'] == 0:
            raise NotFound(detail='No drivers found')
        return Response(drivers,status=status.HTTP_200_OK)
    

class HoursWorked(GenericAPIView):
    def get(self,request,*args,**kwargs):
        # get hours worked 
        #  order descending
        try:
            # hours = Shift.objects.values('hours_worked').order_by('-hours_worked')
            hours = Shift.objects.exclude(hours_worked__lte=15).order_by('-hours_worked')
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if hours is None:
            raise NotFound(detail='No hours found')
        serializer = HoursWorkedSerializer(hours,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
"""
bonus only for the drivers that have exeeded 20 hours of working
"""

class Bonus(GenericAPIView):
    def get(self,request,*args,**kwargs):
        # get hours worked 
        #  order descending
        try:
            bonus_shifts = Shift.objects.filter(hours_worked__gte=10).order_by('-hours_worked')
            bonus = bonus_shifts.annotate(added_bonus=F('hours_worked') * F('payment_per_hour') + 100)

        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if bonus is None:
            raise NotFound(detail='No hours found')
        serializer = BonusSerializer(bonus,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
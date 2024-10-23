from rest_framework.response import Response
from rest_framework import status
from .models import Driver
from .serializers import DriverSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import NotFound
from rest_framework.mixins import UpdateModelMixin
from rest_framework.generics import GenericAPIView
from .permissions import IsAuthenticatedAndUser
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404


class Sign_up(ViewSet): 
    def create(self,request):
        serializer = DriverSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)


class List_Drivers(ViewSet):
    permission_classes=[IsAdminUser]
    def list(self,request):
        queryset = Driver.objects.all()
        serializer = DriverSerializer(queryset,many=True) 
        return Response(serializer.data ,status=status.HTTP_200_OK)


class Remove_driver(ViewSet):
    permission_classes = [IsAdminUser]

    def destroy(self,request,pk=None):
        user = self.request.data.get('username')
        if not user:
            return Response({'error':'no user provided'},status=status.HTTP_400_BAD_REQUEST)

        try:
            driver = Driver.objects.get(username=user) 
            driver.delete()
            return Response({'success':f'driver with username {user} removed'},status=status.HTTP_200_OK)

        except Driver.DoesNotExist:
            raise NotFound(detail=f'no driver with the username {user} found')


# upadating the password
class Update_password(GenericAPIView,UpdateModelMixin):
    permission_classes = [IsAuthenticatedAndUser]
    
    def get_object(self):
        username = self.request.user.username
        try:
            return Driver.objects.get(username=username)
        except Driver.DoesNotExist:
            raise NotFound(detail=f'no driver with the username {username} found')

    def patch(self,request,*args,**kwargs):
        new_password = request.data.get('password')
        confirm_new_passowrd = request.data.get('confirm_password')

        if not new_password or not confirm_new_passowrd:
            return Response({'error':'no password or confirm_password provided'},status=status.HTTP_400_BAD_REQUEST)
        
        if new_password != confirm_new_passowrd:
            return Response({'error':'passwords do not match'},status=status.HTTP_400_BAD_REQUEST)
        
        driver = self.get_object()
        self.check_object_permissions(request,driver)
        update_data = {'password':new_password,'confirm_password':confirm_new_passowrd}
        serializer = DriverSerializer(driver,data=update_data,partial=True)
        if serializer.is_valid():
            driver.password = make_password(new_password)
            driver.save()
            return Response({'successs':'Password updated'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# getting a driver without using authentication
class GetDriverName(ViewSet):
    def retrieve (self,request):
        name = self.request.query_params.get('name')
        if name is None :
            return Response({'error':'no name provided'},status=status.HTTP_400_BAD_REQUEST)
    
        try:
            driver = Driver.objects.get(username__iexact=name)
        except Driver.DoesNotExist:
            raise NotFound(detail=f'no driver with the name {name} found')
        
        serializer = DriverSerializer(driver)
        return Response(serializer.data,status=status.HTTP_200_OK)

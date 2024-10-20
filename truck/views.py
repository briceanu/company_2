from rest_framework.mixins import ListModelMixin,CreateModelMixin 
from rest_framework.generics import GenericAPIView
from .models import Truck
from .serializers import TruckSerializer
from rest_framework.permissions import IsAdminUser


class List_Truck(GenericAPIView, ListModelMixin):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAdminUser]

    def get(self,request,*args,**kwargs):
        return self.list(self,request,*args,**kwargs)
        



class Create_Truck(GenericAPIView,CreateModelMixin):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAdminUser]

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
 



 

 


 
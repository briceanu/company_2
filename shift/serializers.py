from rest_framework import serializers
from .models import Shift

class ShiftSerializer(serializers.ModelSerializer):
    daily_payment = serializers.SerializerMethodField(read_only=True)

    class Meta:
        fields = "__all__"
        model = Shift


    def get_daily_payment(self,obj):
        return obj.payment_per_day
    


class HoursWorkedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['hours_worked']

class BonusSerializer(serializers.ModelSerializer):
    added_bonus = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Shift
        fields = ['truck_used','driver_id','hours_worked','hours_worked','weight_carried','added_bonus'
                  ,'payment_per_hour']
    
    def get_added_bonus(self,obj):
        return obj.added_bonus
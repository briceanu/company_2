from rest_framework import serializers
from .models import Shift

class DriverSerializer(serializers.ModelSerializer):
    daily_payment = serializers.SerializerMethodField(read_only=True)

    class Meta:
        fields = ["__all__"]
        model = Shift


    def get_payment_per_day(self,obj):
        return obj.payment_per_day
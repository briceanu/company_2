from rest_framework import serializers
from .models import Shift

class ShiftSerializer(serializers.ModelSerializer):
    daily_payment = serializers.SerializerMethodField(read_only=True)

    class Meta:
        fields = "__all__"
        model = Shift


    def get_daily_payment(self,obj):
        return obj.payment_per_day
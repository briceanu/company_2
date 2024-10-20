from rest_framework import serializers
from .models import Driver
from rest_framework.exceptions import ValidationError
import re
from .models import Driver


class DriverSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        fields = ['username','password','email','confirm_password','driver_id']
        model = Driver



    def validate_password(self,value):
        if not re.search(r'[A-Z]',value):
            raise ValidationError(detail='password must contain one upperase')

        if len(value)< 8:
            raise ValidationError(detail='password must be at leat 8 characters')
        if not re.search(r'\d',value):
            raise ValidationError(detail='password must contain at least one number')
        return value
    

    def validate(self,data):
        # check tho see if passwords match 
        if data.get('password') != data.get('confirm_password'):
            raise ValidationError(detail='Passwords do not match')
        # check to see if username already exists
        if Driver.objects.filter(username=data.get('username')).exists():
            raise ValidationError('Username already exists')
        # check to see if email already exists
        if Driver.objects.filter(email=data.get('email')).exists():
            raise ValidationError({'email': 'Email already exists.'})

        return data



    def create(self, validated_data):
        validated_data.pop('confirm_password') 
        user = Driver(**validated_data)
        user.set_password(validated_data['password']) 
        user.save()
        return user
        
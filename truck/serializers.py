from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Truck

class TruckSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Truck

    # validating truck brand
    def validate_truck_brand(self, value):
        allowed_brands = ["Mercedes_Benz", 'Scania', 'Volvo']
        if value not in allowed_brands:
            raise ValidationError('Only these brands allowed: Mercedes_Benz, Scania, Volvo')
        return value

    # overriding the general validate method to validate truck model based on brand
    def validate(self, data):
        truck_brand = data.get('truck_brand')
        truck_model = data.get('truck_model')

        # Perform model validation based on brand
        if truck_brand == 'Scania':
            allowed_models = ["G 500", 'P 300']
            if truck_model not in allowed_models:
                raise ValidationError({'truck_model': 'Only these models are allowed for Scania: G 500 and P 300'})

        elif truck_brand == 'Mercedes_Benz':
            allowed_models = ["Axor", 'Actros']
            if truck_model not in allowed_models:
                raise ValidationError({'truck_model': 'Only these models are allowed for Mercedes_Benz: Axor and Actros'})

        elif truck_brand == 'Volvo':
            allowed_models = ["FH17", 'FL']
            if truck_model not in allowed_models:
                raise ValidationError({'truck_model': 'Only these models are allowed for Volvo: FH17 and FL'})

        return data

    # validating color
    def validate_color(self, value):
        allowed_colors = ['black', 'green', 'blue', 'white']
        if value not in allowed_colors:
            raise ValidationError('Only these colors are allowed: black, green, blue, white')
        return value

    # validating fuel type
    def validate_fuel_type(self, value):
        allowed_fuel_type = ['Diesel', 'LPG Gas']
        if value not in allowed_fuel_type:
            raise ValidationError('Only these fuel types are allowed: diesel, LPG Gas')
        return value

from rest_framework import serializers
from .models import Booking, Menu

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'no_of_guests', 'bookingDate']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
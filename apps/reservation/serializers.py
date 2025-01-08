from rest_framework import serializers
from apps.reservation.models import Restaurant
from apps.reservation.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['restaurant', 'reservation_time', 'number_people']
        extra_kwargs = {"user": {"required": False}}


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['title', 'address', 'description', 'resized_image', 'available_sits']


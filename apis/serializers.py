from rest_framework import serializers

from hotels.models import Hotel, Room, Inventory


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "code",
        )
        model = Hotel


class HotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "code",
        )
        model = Hotel


class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "code",
        )
        model = Room

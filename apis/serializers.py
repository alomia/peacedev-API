from rest_framework import serializers

from hotels.models import Hotel, Room


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
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


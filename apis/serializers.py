from rest_framework import serializers

from hotels.models import Hotel


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

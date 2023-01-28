from rest_framework import serializers

from hotels.models import Hotel, Inventory


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


class InventoryDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="rate.room.name", read_only=True)
    code = serializers.CharField(source="rate.room.code", read_only=True)

    class Meta:
        fields = (
            "name",
            "code",
            "price",
            "allotment",
        )
        model = Inventory

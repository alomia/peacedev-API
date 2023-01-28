from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Sum

from hotels.models import Hotel, Inventory
from .serializers import (
    HotelListSerializer,
    HotelDetailSerializer,
    InventoryDetailSerializer,
)


class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer


class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer

    lookup_field = "code"


class InventoryList(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryDetailSerializer

    def get_queryset(self):
        hotel_code = self.kwargs["code"]
        checkin_date = self.kwargs["checkin_date"]
        checkout_date = self.kwargs["checkout_date"]
        return Inventory.objects.filter(
            rate__room__hotel=hotel_code,
            rate__room__checkin_date__lte=checkin_date,
            rate__room__checkout_date__gte=checkout_date,
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        count = queryset.count()
        total_price = queryset.aggregate(total_price=Sum("price"))["total_price"]
        for inventory in queryset:
            inventory.allotment = count
            inventory.save()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        response_data = {"total_price": total_price, "breakdown": data}
        return Response(response_data)

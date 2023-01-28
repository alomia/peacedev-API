from rest_framework import generics

from hotels.models import Hotel, Room
from .serializers import HotelListSerializer, HotelDetailSerializer, RoomDetailSerializer


class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer


class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer

    lookup_field = "code"


class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

    def get_queryset(self):
        hotel_code = self.kwargs['code']
        checkin_date = self.kwargs['checkin_date']
        checkout_date = self.kwargs['checkout_date']
        return Room.objects.filter(hotel=hotel_code, checkin_date__lte=checkin_date, checkout_date__gte=checkout_date)

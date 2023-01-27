from rest_framework import generics

from hotels.models import Hotel
from .serializers import HotelListSerializer, HotelDetailSerializer


class HotelList(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer


class HotelDetail(generics.RetrieveDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer

    def get_object(self):
        hotel_code = self.kwargs["hotel_code"]
        return self.queryset.get(code=hotel_code)

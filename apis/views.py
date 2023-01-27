from rest_framework import generics

from hotels.models import Hotel
from .serializers import HotelSerializer


class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetail(generics.RetrieveDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

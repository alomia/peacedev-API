from django.urls import path

from .views import HotelList, HotelDetail, RoomList

urlpatterns = [
    path("availability/<int:pk>/<str:checkin_date>/<str:checkout_date>/", RoomList.as_view(), name="room_list"),
    path("hotels/<int:pk>/", HotelDetail.as_view(), name="hotel_detail"),
    path("hotels/", HotelList.as_view(), name="hotel_list"),
]

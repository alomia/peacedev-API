from django.urls import path

from .views import HotelList, HotelDetail, RoomList

urlpatterns = [
    path("availability/<str:code>/<str:checkin_date>/<str:checkout_date>/", RoomList.as_view(), name="room_list"),
    path("hotels/<str:code>/", HotelDetail.as_view(), name="hotel_detail"),
    path("hotels/", HotelList.as_view(), name="hotel_list"),
]

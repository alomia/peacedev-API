from django.urls import path

from .views import HotelList, HotelDetail

urlpatterns = [
    path("hotels/<str:hotel_code>/", HotelDetail.as_view(), name="hotel_detail"),
    path("hotels/", HotelList.as_view(), name="hotel_list"),
]

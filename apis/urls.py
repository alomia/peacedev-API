from django.urls import path

from .views import HotelList, HotelDetail

urlpatterns = [
    path("hotels/<int:pk>/", HotelDetail.as_view(), name="hotel_detail"),
    path("hotels/", HotelList.as_view(), name="hotel_list"),
]

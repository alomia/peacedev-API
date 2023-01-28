from django.urls import path

from .views import HotelList, HotelDetail, InventoryList

urlpatterns = [
    path(
        "availability/<str:code>/<str:checkin_date>/<str:checkout_date>/",
        InventoryList.as_view(),
        name="inventory_list",
    ),
    path("hotels/<str:code>/", HotelDetail.as_view(), name="hotel_detail"),
    path("hotels/", HotelList.as_view(), name="hotel_list"),
]

from django.contrib import admin

from .models import Hotel, Room, Rate, Inventory

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Rate)
admin.site.register(Inventory)

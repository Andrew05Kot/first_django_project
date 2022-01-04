from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Station

@admin.register(Station)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')


# super_admin
# admin
# kotygaandrey05@gmail.com
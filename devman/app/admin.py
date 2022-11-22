from django.contrib import admin

from .models import GeoJSON


# Register your models here.
@admin.register(GeoJSON)
class RecordGeoJSON(admin.ModelAdmin):
    fields = ("title", "description_short", "description_long", ("lng", "lat"))

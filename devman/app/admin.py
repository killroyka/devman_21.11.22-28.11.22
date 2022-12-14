from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import GeoJSON, GeoImage


class GeoImageInline(admin.TabularInline):
    model = GeoImage


@admin.register(GeoJSON)
class GeoJSONAdmin(admin.ModelAdmin):
    fields = ("title", "description_short", "description_long", ("lng", "lat"))
    inlines = [
        GeoImageInline
    ]
    ordering = ('title',)
    list_display = ("title", "description_short")




@admin.register(GeoImage)
class GeoImageAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ("geojson", "index", "headshot_image")
    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url=obj.img.url,
            height=min(200, obj.img.height),
        )
        )

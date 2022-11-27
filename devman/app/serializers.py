from rest_framework import serializers

from .models import GeoJSON, GeoImage


class GeoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoImage
        fields = ("img",)


class GeoJSONSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = GeoJSON
        fields = ("title", "description_short", "description_long", "lng", "lat")
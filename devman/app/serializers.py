from rest_framework import serializers

from .models import GeoJSON, GeoImage


class GeoJSONSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoJSON
        exclude = ("id",)

class GeoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoImage
        exclude = ("id", "index")
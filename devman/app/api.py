from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GeoJSONSerializer, GeoImageSerializer
from .models import GeoJSON, GeoImage
from pprint import pprint

@api_view(['GET'])
def GeoJSONDetail(request, pk):
    try:
        geojson = GeoJSON.objects.get(id=pk)
    except GeoJSON.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        images = GeoImage.objects.all().filter(geojson=geojson.id)
        geojson = GeoJSONSerializer(geojson).data
        geojson["imgs"] = []
        for image in images:
            geojson["imgs"].append(GeoImageSerializer(image).data["img"])
        geojson["coordinates"] = {
            "lng": geojson["lng"],
            "lat": geojson["lat"]
        }
        del geojson["lat"]
        del geojson['lng']
        pprint(geojson)
        return Response(geojson)

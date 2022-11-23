from django.views.generic import ListView
from .models import GeoJSON
from django.views.generic import ListView
from django.conf import settings
from .models import GeoJSON


# Create your views here.

class HomepageView(ListView):
    template_name = "index.html"
    model = GeoJSON

    def get_context_data(self, *, object_list=None, **kwargs):
        return {"context": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [37.62, 55.793676]
                    },
                    "properties": {
                        "title": "«Легенды Москвы",
                        "placeId": "moscow_legends",
                        "detailsUrl": 'staticfiles/places/moscow_legends.json'
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [37.64, 55.753676]
                    },
                    "properties": {
                        "title": "Крыши24.рф",
                        "placeId": "roofs24",
                        "detailsUrl": "staticfiles/places/roofs24.json"
                    }
                }
            ]
        }}

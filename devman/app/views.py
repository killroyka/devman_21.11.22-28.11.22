from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import GeoJSON
from django.views.generic import ListView, DetailView

from .models import GeoJSON


# Create your views here.

class HomepageView(ListView):
    template_name = "index.html"
    model = GeoJSON

    def get_context_data(self, *, object_list=None, **kwargs):
        context = GeoJSON.objects.all()
        return {'GeoJSONs': context}


class GeoJSONDetail(DetailView):
    model = GeoJSON
    template_name = "details/GeoJSON.html"
    context_object_name = "geojson"

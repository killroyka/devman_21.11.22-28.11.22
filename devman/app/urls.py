from django.contrib import admin
from django.urls import path
from .views import HomepageView, GeoJSONDetail
from .api import GeoJSONDetail

urlpatterns = [
    path("", HomepageView.as_view(), name="mainpage"),
    path("places/<int:pk>", GeoJSONDetail, name="GeoJSONDetail"),
]

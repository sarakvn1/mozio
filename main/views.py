from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet, ModelViewSet
from shapely.geometry import Polygon, Point, LineString, MultiPolygon, MultiPoint, MultiLineString

from main.geo_json import GeoJson
from main.serializers import ProviderSerializer, ServiceAreaSerializer
from main.models import Provider, ServiceArea


class ProviderView(ModelViewSet):
    serializer_class = ProviderSerializer

    def get_queryset(self):
        return Provider.objects.all()

    # Because we are only going to deal with retrieving the current users data,
    # we are forced to close off all other routes.

    # def create(self, request, *args, **kwargs):
    #     pass
    #
    # def retrieve(self, request, *args, **kwargs):
    #     pass
    #
    # def update(self, request, *args, **kwargs):
    #     pass
    #
    # def partial_update(self, request, *args, **kwargs):
    #     pass
    #
    # def destroy(self, request, *args, **kwargs):
    #     pass


class ServiceAreaView(ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            all_areas = ServiceArea.objects.all()
            data = request.data
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            result = []
            chose_point = Point(latitude, longitude)
            geo_json = GeoJson()
            ge_json_types = ['Point', 'LineString', 'Polygon', 'MultiPoint', 'MultiLineString', 'MultiPolygon']
            for i in all_areas:
                if i.geo_json.get('type') == 'FeatureCollection':
                    feature_list = i.geo_json.get('features')
                    for j in feature_list:
                        geometry_type = j.get('geometry').get('type')
                        coordinates = j.get('geometry').get('coordinates')

                        is_contain = getattr(geo_json, geometry_type.lower())(coordinates, chose_point)
                        if is_contain is True:
                            result.append(i.id)

            r = ServiceArea.objects.filter(id__in=result)
        except Exception as e:
            r = []
        return Response(r)

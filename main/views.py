import loguru
from django.shortcuts import render

# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet, ModelViewSet
from shapely.geometry import Polygon, Point, LineString, MultiPolygon, MultiPoint, MultiLineString

from main.geo_json import GeoJson
from main.serializers import ProviderSerializer, ServiceAreaSerializer, ServiceAreaResponseSerializer, PolygonSerializer
from main.models import Provider, ServiceArea


class ProviderView(ModelViewSet):
    serializer_class = ProviderSerializer

    def get_queryset(self):
        return Provider.objects.all()


class ServiceAreaView(ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    response_schema_dict = {
        "200": openapi.Response(
            description="list of all polygons that include the given lat/lng.",
            examples={
                "application/json": {
                    "id":1,
                    "provider": "sara",
                    "name": "sara2",
                    "price": 123,
                }
            }
        ),

    }
    @swagger_auto_schema(responses=response_schema_dict,operation_description="get all polygons that contains input point",
                         request_body=PolygonSerializer, )
    @action(detail=False, methods=['POST'])
    def polygon(self, request, *args, **kwargs):
        try:
            all_areas = ServiceArea.objects.all()
            serializer = PolygonSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            latitude = float(serializer.data.get('latitude'))
            longitude = float(serializer.data.get('longitude'))
            result = []
            chose_point = Point(longitude, latitude)
            geo_json = GeoJson()
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
            serializer = ServiceAreaResponseSerializer(r, many=True)
        except Exception as e:
            loguru.exception(e)
            raise e
        return Response(serializer.data)

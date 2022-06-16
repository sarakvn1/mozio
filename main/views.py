from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet, ModelViewSet
from shapely.geometry import Polygon, Point

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
        all_areas = ServiceArea.objects.all()
        data = request.data
        lattitude = data.get('lattitude')
        longitude = data.get('longitude')
        result = []
        point = Point(lattitude, longitude)
        for i in all_areas:
            coordinates = i.polygon()
            polygon = Polygon([tuple(i) for i in coordinates[0]])
            if polygon.contains(point) is True:
                result.append(i.id)
        r = ServiceArea.objects.filter(id__in=result)
        return Response(r)

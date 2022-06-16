from django.db import models
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}-{self.name}"


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=50, decimal_places=2),
    geo_json = models.JSONField()

    def __str__(self):
        return f"{self.provider}-{self.name}"

    def polygon(self):
        polygon_list = []
        ge_json_types = ['Point', 'LineString', 'Polygon', 'MultiPoint', 'MultiLineString', 'MultiPolygon']
        if self.geo_json.get('type') == 'FeatureCollection':
            feature_list = self.geo_json.get('features')
            coordinates = []
            for i in feature_list:
                if i.get('geometry').get('type') is not None and i.get('geometry').get('type') == 'Polygon':
                    coordinates = [l for l in i.get('geometry').get('coordinates')]

            # polygon_list = [Polygon(tuple()) for i in coordinates[0]]

        return coordinates

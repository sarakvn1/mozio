from rest_framework import serializers
from main.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ['id', 'name', 'geo_json', 'provider', 'polygon']

    def validate(self, attrs):
        geo_json = attrs.get('geo_json')
        return attrs

from rest_framework import serializers
from main.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ['id', 'name', 'geo_json', 'price', 'provider']

    def validate(self, attrs):
        geo_json = attrs.get('geo_json')
        return attrs


class ServiceAreaResponseSerializer(serializers.ModelSerializer):
    provider = serializers.SerializerMethodField()

    class Meta:
        model = ServiceArea
        fields = ['id', 'name', 'provider', 'price']

    def get_provider(self, instance):
        return instance.provider.name


class PolygonSerializer(serializers.Serializer):
    longitude = serializers.CharField()
    latitude = serializers.CharField()

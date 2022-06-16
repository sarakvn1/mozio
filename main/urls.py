from django.urls import include, path
from rest_framework.routers import DefaultRouter
from drf_yasg.utils import swagger_auto_schema

from main.views import ProviderView,ServiceAreaView

router = DefaultRouter()
router.register(r'provider', ProviderView, basename='providers')
router.register(r'service/area', ServiceAreaView, basename='providers')
urlpatterns = [
    path('', include(router.urls)),
]

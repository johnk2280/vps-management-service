from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import VPSModelViewSet

router = DefaultRouter()
router.register('vps_objects', VPSModelViewSet, basename='vps_objects')

urlpatterns = [
    path('', include(router.urls)),
]

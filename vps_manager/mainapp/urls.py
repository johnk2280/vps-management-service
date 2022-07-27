from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import VPSModelViewSet
from .views import VPSRetrieveUpdateViewSet

router = DefaultRouter()
router.register(
    'vps_objects',
    VPSModelViewSet,
    basename='vps_objects',
)
router.register(
    'vps_objects/<int:uid>/',
    VPSRetrieveUpdateViewSet,
    basename='vps_retrieve_update',
)

urlpatterns = [
    path('', include(router.urls)),
]

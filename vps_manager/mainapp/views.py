from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from .models import VPS
from .serializers import VPSSerializer


class VPSModelViewSet(ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('uid', 'cpu', 'ram', 'hdd', 'status')

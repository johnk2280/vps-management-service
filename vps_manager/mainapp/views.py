from rest_framework.viewsets import ModelViewSet

from .models import VPS
from .serializers import VPSSerializer


class VPSModelViewSet(ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer

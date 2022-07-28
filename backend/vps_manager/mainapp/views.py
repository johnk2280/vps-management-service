from rest_framework.viewsets import ModelViewSet, ViewSetMixin
from rest_framework.generics import RetrieveUpdateAPIView

from django_filters.rest_framework import DjangoFilterBackend

from .models import VPS
from .serializers import VPSSerializer


class VPSModelViewSet(ModelViewSet):
    """
    Creating a VPS object and getting a list of VPS objects.
    """
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('uid', 'cpu', 'ram', 'hdd', 'status')


class VPSRetrieveUpdateViewSet(ViewSetMixin, RetrieveUpdateAPIView):
    """
    Getting VPS object by uid and updating VPS object status.
    """
    queryset = VPS.objects.all()
    lookup_field = 'uid'

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = VPSSerializer
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = VPSSerializer
        return super().update(request, *args, **kwargs)

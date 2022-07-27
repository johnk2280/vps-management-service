from rest_framework import serializers

from .models import VPS


class VPSSerializer(serializers.ModelSerializer):
    """
    Serializer for VPS model.
    """
    class Meta:
        model = VPS
        fields = (
            'uid',
            'cpu',
            'ram',
            'hdd',
            'status',
            'created_at',
            'updated_at',
        )

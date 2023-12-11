from .models import VendorModel
from rest_framework import serializers

class VendorSerializer(serializers.Serializer):
    class Meta:
        model = VendorModel
        fields = "__all__"
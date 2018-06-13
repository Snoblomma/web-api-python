from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Place
        fields = ('place_id', 'name', 'visited', 'types', 'created_at', 'updated_at')
        read_only_fields = ('place_id', 'name', 'visited', 'types', 'created_at', 'updated_at')
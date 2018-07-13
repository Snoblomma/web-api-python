from rest_framework import serializers
from .models import Place
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category 
        fields = ('name', 'description')
        read_only_fields = ('name', 'description')

class PlaceSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Place
        fields = ('place_id', 'name', 'visited', 'category', 'created_at', 'updated_at')
        read_only_fields = ('place_id', 'name', 'visited', 'category', 'created_at', 'updated_at')
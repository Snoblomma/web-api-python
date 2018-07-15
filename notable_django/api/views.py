from django.shortcuts import render

from rest_framework import generics
from .serializers import PlaceSerializer
from .serializers import CategorySerializer
from .models import Place
from .models import Category

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()

class PlaceView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
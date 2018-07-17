from django.shortcuts import render

from rest_framework import generics
from .serializers import PlaceSerializer
from .serializers import CategorySerializer
from .models import Place
from .models import Category
from .forms import CategoryForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import ListView
from django.views import View

class CategoryView(View):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    # model = Category

    # def perform_create(self, serializer):
    #     serializer.save()
    def get(self, request, *args, **kwargs):
        # queryset = Category.objects.all()
        category_list = Category.objects.order_by('name')
        output = ', '.join([q.name for q in category_list])
        responseData = {
            'id': 4,
            'name': 'Test Response',
            'roles' : ['Admin','User']
        }
        return JsonResponse(output, safe=False)

    def post(self, request, *args, **kwargs):
        a = {
            "name": "this is name"
        }
        f = CategoryForm(request.POST, instance=a)
        f.save()
        responseData = {
            'id': 4,
            'success': 'Test Response',
            'roles' : ['Admin','User']
        }
        return JsonResponse(responseData, safe=False)


class PlaceView(View):
    # queryset = Place.objects.all()
    # serializer_class = PlaceSerializer

    # model = Place

    # def perform_create(self, serializer):
    #     serializer.save()

    # def head(self, *args, **kwargs):
    #     data = {
    #     'name': 'Vitor',
    #     'location': 'Finland',
    #     'is_active': True,
    #     'count': 28
    # }
    #     return JsonResponse(data)
    def get(self, request, *args, **kwargs):
        queryset = Place.objects.all()
        places_list = Place.objects.order_by('name')
        output = ', '.join([q.name for q in places_list])
        responseData = {
            'id': 4,
            'name': 'Test Response',
            'roles' : ['Admin','User']
        }
        return JsonResponse(output, safe=False)

    def post(self, request, *args, **kwargs):
        responseData = {
            'id': 4,
            'success': 'Test Response',
            'roles' : ['Admin','User']
        }
        return JsonResponse(responseData, safe=False)
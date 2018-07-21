from django.shortcuts import render
import json

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
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    model = Category

    # def perform_create(self, serializer):
    #     serializer.save()
    def get(self, request, *args, **kwargs):
        category_list = Category.objects.order_by('name')
        output = []
        for q in category_list:
            output.append(str(q.auto_id) + ": " + q.name)
        return JsonResponse(output, safe=False)

    def post(self, request, *args, **kwargs):
        # a = {
        #     "name": "this is name"
        # }
        # f = CategoryForm(request.POST, instance=a)
        # Category.objects. perform_create(name='some_name')
        # f.save()
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        name = body['name']
        b2 = Category(name = name)
        b2.save()
        responseData = {
            'success': name
        }
        return JsonResponse(responseData, safe=False)


class PlaceView(View):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    model = Place

    def get(self, request, *args, **kwargs):
        places_list = Place.objects.order_by('name')
        output = ', '.join([q.name for q in places_list])
        return JsonResponse(output, safe=False)

    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        name = body['name']
        place_id = body['place_id']
        visited = body['visited']
        category = body['category']
        test = Category(name = "this is test")
        b2 = Place(visited = visited)
        b2.save()
        b2.place_id = place_id
        b2.name = name
        b2.visited = 'true'
        # b2 = Place(place_id = place_id, name = name, visited = visited)
        # b2.save()
        b2.category.set(test)
        b2.save()
        responseData = {
            'success': 'wow!'
        }
        return JsonResponse(responseData, safe=False)
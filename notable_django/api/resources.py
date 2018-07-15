from tastypie.resources import ModelResource
from api.models import Place
from api.models import Category
from tastypie.authorization import Authorization

class PlaceResource(ModelResource):
    class Meta:
        queryset = Place.objects.all()
        resource_name = 'place'
        authorization = Authorization()
        fields = ['place_id', 'name', 'visited', 'category', 'created_at', 'updated_at']

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authorization = Authorization()
        fields = ['name']
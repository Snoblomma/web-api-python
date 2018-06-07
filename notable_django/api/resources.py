from tastypie.resources import ModelResource
from api.models import Place
from tastypie.authorization import Authorization

class PlaceResource(ModelResource):
    class Meta:
        queryset = Place.objects.all()
        resource_name = 'place'
        authorization = Authorization()
        fields = ['place_id', 'name', 'added_at', 'visited']
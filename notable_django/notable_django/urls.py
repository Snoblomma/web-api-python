from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from api.resources import PlaceResource
from api.views import CreateView

place_resource = PlaceResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(place_resource.urls))
]


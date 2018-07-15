from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from api.resources import PlaceResource
from api.resources import CategoryResource
from api.views import PlaceView
from api import views

place_resource = PlaceResource()
category_resource = CategoryResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', views.PlaceView.as_view()),
    url(r'^api/', views.CategotyView.as_view())
]


from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from api.resources import PlaceResource
from api.resources import CategoryResource
from api import views

place_resource = PlaceResource()
category_resource = CategoryResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('place/', views.PlaceView.as_view()),
    path('category/', views.CategoryView.as_view())
]


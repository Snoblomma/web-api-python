from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from api.resources import NoteResource
from api.views import CreateView

note_resource = NoteResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(note_resource.urls)),
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
]


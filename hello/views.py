from django.shortcuts import render
from django.http import HttpResponse

from .models import Places
import requests
import os

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)


def db(request):

    places = Places()
    places.save()
    places = Places.objects.all()
    return HttpResponse(places)

def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'github.html', {'user': user})


def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return HttpResponse(geodata['country_name'])
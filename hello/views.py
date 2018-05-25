from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests
import os

# Create your views here.
def index(request):
    # r = requests.get('http://httpbin.org/status/418')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'core/github.html', {'user': user})
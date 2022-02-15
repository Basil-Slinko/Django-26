import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    1 / 0
    return HttpResponse('Hello from Django!')


def time(request):
    current_time = datetime.datetime.now().time()
    return HttpResponse(f'Time = {current_time}')

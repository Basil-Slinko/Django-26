from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations_view(request):
    content = list()
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            content.append(row)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)

    bus_stations = paginator.page(page_number)

    context = {
        'bus_stations': bus_stations,
        'page': page,
    }

    return render(request, 'stations/index.html', context)

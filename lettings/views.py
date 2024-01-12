from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Letting


def lettings_index(request: HttpRequest) -> HttpResponse:
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings_index.html", context)


def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "letting.html", context)

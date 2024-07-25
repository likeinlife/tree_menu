from django.http import HttpRequest
from django.shortcuts import render


def home(request: HttpRequest, *_, **__):
    return render(request, "index.html")

from django.http import HttpResponse
from django.shortcuts import render


def posts_urls(request):
    return HttpResponse("Page Posts Touched")

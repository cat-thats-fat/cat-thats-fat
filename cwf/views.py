from django.shortcuts import render
from django.http import HttpResponse

def cwf(request):
    return HttpResponse("<h1>Cheap Weed Finder</h1>")


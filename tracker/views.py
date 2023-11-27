from django.shortcuts import render
from django.http import HttpResponse

def tracker(request):
    return HttpResponse("<h1>Sesh Tracker</h1>")
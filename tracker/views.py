from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def tracker(request):
    return HttpResponse("<h1>Sesh Tracker</h1>")
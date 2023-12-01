from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home/home.html')

@login_required
def cwfBTN(request):
    return redirect('cwf')


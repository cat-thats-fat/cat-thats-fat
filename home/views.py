from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'home/home.html')

def cwfBTN(request):
    return redirect('cwf')
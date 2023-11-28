from django.shortcuts import render, redirect
from django.http import HttpResponse

def cwf(request):
    return render(request, 'cwf/cwf.html')

def backBTN(request):
    return redirect('home')


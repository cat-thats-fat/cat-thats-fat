from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'login/login.html', {'message': 'idle'})

def login_submit (requests):

    return render(requests, 'login/login.html', {'message': 'login invalid'})

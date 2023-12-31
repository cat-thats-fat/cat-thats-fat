from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login as login_auth


class CustomLoginView(LoginView):
    template_name = 'login/login.html'

@never_cache
def login(request):
    return render(request, 'login/login.html', {'message': 'idle'})


def login_submit(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_auth(request, user)
            return redirect('../home')
        else:
            return render(request, 'login/login.html', {'message': 'invalid login'})
    else:
        if request.user.is_authenticated:
            return redirect('../home')
        else:
            return render(request, 'login/login.html', {'message': 'unauthorized'})
            
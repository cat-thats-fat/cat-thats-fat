from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.login, name='login-home'),
    path('login_submit', views.login_submit, name='login_submit'),
    path('login_submit', include('home.urls')),
]
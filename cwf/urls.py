from django.urls import path
from . import views


urlpatterns = [
    path('', views.cwf, name='cwf-home'),
]
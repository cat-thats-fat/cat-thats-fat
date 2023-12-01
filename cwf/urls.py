from home import views as home_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cwf, name='cwf'),
    path('backBTN/', views.backBTN, name='backBTN'),
    path('cwfdata/', views.cwfdata, name='cwfdata')
]
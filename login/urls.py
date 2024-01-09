from django.urls import include, path
from . import views as login_views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns = [
    path('', login_views.login, name='login'),
    path('login_submit', login_views.login_submit, name='login_submit'),
\
]
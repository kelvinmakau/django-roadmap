from django.urls import path
from . import views

# URLS
urlpatterns = [
    path('', views.home, name='posts'),
]
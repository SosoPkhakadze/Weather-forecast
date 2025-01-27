from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('weather/weather_search.html', views.weather_search, name='weather_search'),
]

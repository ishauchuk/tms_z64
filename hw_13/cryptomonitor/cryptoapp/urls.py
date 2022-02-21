from django.urls import path

from .views import *

urlpatterns = [
    path('', home),
    path('btc/', bitcoin),
    path('eth/', ethereum),
    path('usdt/', tether),
]

# quick_publisher/urls.py
from django.urls import path

from .views import maps, polls_list, index, telecomando

urlpatterns = [
    path('', index, name='index'),
    path('maps', maps, name='maps'),
    path('telecomando', telecomando, name='telecomando'),
    path('api', polls_list, name="polls_list"),
]

from django.urls import path
from blackout.views import index, hacker_etico

urlpatterns = [
    path('', index, name='index'),
    path('comprar/hacker_etico', hacker_etico, name='hacker_etico'),
]

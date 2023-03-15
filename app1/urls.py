from django.urls import path 
from app1.views import *
app_name='smg'
urlpatterns=[
    path('prathyu/',prathyu,name='prathyu'),
]
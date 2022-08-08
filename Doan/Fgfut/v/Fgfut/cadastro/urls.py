
from django.urls import path

from . import views

urlpatterns = [
    path('', views.telacadastro, name='index'),
]



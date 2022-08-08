

# Create your views here.
from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import TemplateView


def telapartidas(request):
    return HttpResponse('partidas ')
# Create your views here.
from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import TemplateView


def telalogin(request):
    return HttpResponse('AE PORRA ')


'''def telalogin(request):
    return render(request, "login/index.html")'''
    
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def january(request):
    return HttpResponse("This is january challenge!")


def february(request):
    return HttpResponse("This is february challenge!")

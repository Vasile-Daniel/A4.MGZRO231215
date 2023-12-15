from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse('I am in home - http response')
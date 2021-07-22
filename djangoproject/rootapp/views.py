from django.shortcuts import render
from django.http import HttpResponse

def root (request):
    return HttpResponse("The server has started")
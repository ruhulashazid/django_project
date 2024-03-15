from django.shortcuts import render, HttpResponse

# Create your views here.

def index (requestr):
    return HttpResponse ("Hello, World!")

def about (requestr):
    return HttpResponse ("About Us")

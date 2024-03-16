from django.shortcuts import render, HttpResponse

# Create your views here.

def index (requestr):
    return HttpResponse ("Hello, World!")

def about (requestr):
    return HttpResponse ("About Us")

def hello (requestr,firstname):
    return HttpResponse (f"Hello, {firstname}")

def add (request,num1,num2):
    return HttpResponse (f"the total number is: {num1 + num2}")

 
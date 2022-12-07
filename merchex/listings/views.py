from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello Django !</h1>')

def index(request):
    return HttpResponse('<h1>Page d\'acceuil !</h1>')

def sign_in(request):
    return HttpResponse('<h1>Page d\'inscription !</h1>')

def flux(request):
    return HttpResponse('<h1>Flux !</h1>')

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, logout, authenticate # import des fonctions login et authenticate
from . import forms
# Create your views here.

def hello(request):
    return render(request, 'hello.html')

def index(request):
    return HttpResponse('<h1>Page d\'acceuil !</h1>')

def logout_user(request):
    
    logout(request)
    return redirect('login')

def sign_in(request):
    return HttpResponse('<h1>Page d\'inscription !</h1>')

def flux(request):
    return HttpResponse('<h1>Flux !</h1>')

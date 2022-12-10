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

# def login_page(request):
#     form = forms.LoginForm()
#     message = ''
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 message = f'Bonjour, {user.username}! Vous êtes connecté.'
#             else:
#                 message = 'Identifiants invalides.'
#     return render(
#         request, 'login.html', context={'form': form, 'message': message})

def sign_in(request):
    return HttpResponse('<h1>Page d\'inscription !</h1>')

def flux(request):
    return HttpResponse('<h1>Flux !</h1>')

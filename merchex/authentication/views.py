from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, logout, authenticate # import des fonctions login et authenticate
from . import forms
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def logout_user(request):
    
    logout(request)
    return redirect('authentication/logout')

@login_required
def hello(request):
    return render(request, 'authentication/hello.html')

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            #auto-login user
            login(request, user)
            return redirect('/login.html')
    return render(request, 'authentication/signup.html', context={'form': form})

class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('authentication/logout')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})

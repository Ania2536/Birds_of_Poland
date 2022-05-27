from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import LoginFormView, RegisterFormView

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = RegisterFormView()
        return render(request, 'form.html', {'form': form})
    def post(self, request):
        form = RegisterFormView(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            mail = form.cleaned_data['mail']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                user = User.objects.create(username=username, email=mail)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                return redirect('main')
            else:
                alert = "Hasła muszą być jednakowe"
        return render(request, 'form.html', {'form': form, 'alert': alert})

class LoginView(View):
    def get(self, request):
        form = LoginFormView()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginFormView(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            return render(request, 'form.html', {'form': form})


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')
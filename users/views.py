from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def connection(request):
    """

        Connect the user
    """
    error = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = LoginForm()
    return render(request, 'users/connection.html', locals())


def register(request):
    """
        Get all the data from
        the register form and create
        an object from the user's models
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username,
                                            email = email,
                                            last_name=last_name,
                                            first_name=first_name,
                                            password=password
                                            )
            return redirect('/connexion')

    else:
        form = RegisterForm()

    return render(request, 'users/register.html', locals())


def disconnection(request):
    """
        Disconnect the user
    """
    logout(request)
    return HttpResponseRedirect('/')

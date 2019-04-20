from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegistrationForm


def home_page(request):
    return render(request, 'home_page.html', {})


def contact(request):
    if request.method == 'POST':
        pass
    else:
        form = ContactForm()
        return render(request, 'contact_page.html', {'form': form})


def about(request):
    return render(request, 'home_page.html', {})


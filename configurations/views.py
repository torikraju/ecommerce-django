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


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}
    print(f'User Logged In: {request.user.is_authenticated}')
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            return redirect('/login')
        else:
            print("error")

    return render(request, 'auth/login.html', context)


def register_page(request):
    form = RegistrationForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(username, email, password)
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.save()
        print(form.cleaned_data)
    return render(request, 'auth/registration.html', context)

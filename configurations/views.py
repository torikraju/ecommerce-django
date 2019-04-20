from django.shortcuts import render

from .forms import ContactForm


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

from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'landing-page.html')

def contact_page(request):
    return render(request, 'contact-page.html')
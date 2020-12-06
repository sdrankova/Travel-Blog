from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import RegisterForm

from destinations.forms import EditCreateForm
from destinations.models import Destination
from .models import UserProfile

def home_page_logged_user(request):
    return render(request, 'landing-page-loggedin.html')


def add_destination(request):
    destination = Destination()
    if request.method == 'GET':
        form = EditCreateForm(instance=destination)

        context = {
            'form': form,
            'destination': destination,
        }

        return render(request, 'destinations/add.html', context)
    else:
        form = EditCreateForm(
            request.POST,
            request.FILES,
            instance=destination,
        )
        if form.is_valid():
            form.save()

            return redirect('description and comment', destination.pk)

        context = {
            'form': form,
            'destination': destination,
        }

        return render(request, 'destinations/edit.html', context)


def profile(request, pk=None):
    pass


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user,
            )
            profile.save()

            login(request, user)
            return redirect('destinations')
        context = {
            'form': form,
        }
        return render(request, 'signup.html', context)

    else:
        form = RegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'signup.html', context)

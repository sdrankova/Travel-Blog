from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import RegisterForm, ProfileForm

from destinations.forms import EditCreateForm
from destinations.models import Destination
from .models import UserProfile

def home_page_logged_user(request):
    return render(request, 'landing-page-loggedin.html')

@login_required
def add_destination(request):
    destination = Destination(current_user=request.user.userprofile)
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
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'destinations': user.userprofile.destination_set.all(),
            'form': ProfileForm(),
        }
        return render(request, 'profile.html', context)

    else:
        form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current profile')
        return redirect('current profile')


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


def signout(request):
    logout(request)
    return redirect('home page')
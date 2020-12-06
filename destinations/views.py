from django.shortcuts import render, redirect

from destinations.forms import CommentForm, EditForm
from destinations.models import Destination, Like, Comment


def all_destinations(request):
    context = {
        'destinations': Destination.objects.all(),
    }
    return render(request, 'destinations/all-destinations.html', context)


def description_and_comment_destination(request, pk):
    destination = Destination.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'destination': destination,
            'form': CommentForm(),
        }
        return render(request, 'destinations/description-destination.html', context)

    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['comment'])
            comment.destination = destination
            comment.save()
            return redirect('description and comment', pk)
        context = {
            'destination': destination,
            'form': form,
        }
        return render(request, 'destinations/description-destination.html', context)


def like_destination(request, pk):
    destination = Destination.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.destination = destination
    like.save()
    return redirect('description and comment', pk)

def edit_destination(request, pk):
    destination = Destination.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditForm(instance=destination)

        context = {
            'form': form,
            'destination': destination,
        }
        return render(request, 'destinations/edit.html', context)
    else:
        form = EditForm(request.POST, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('description and comment', destination.pk)
        context = {
            'form': form,
            'destination': destination,
        }
        return render(request, 'destinations/edit.html', context)

def delete(request, pk):
    destination = Destination.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'destination': destination,
        }
        return render(request, 'destinations/delete.html', context)
    else:
        destination.delete()
        return redirect('destinations')
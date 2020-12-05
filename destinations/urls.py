from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_destinations, name='destinations'),
    path('description/<int:pk>/', views.description_and_comment_destination, name='description and comment'),
    path('like/<int:pk>/', views.like_destination, name='like'),
]
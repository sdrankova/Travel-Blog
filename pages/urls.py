from django.urls import path, include

from . import views

urlpatterns = [
    path('main-page/', views.home_page, name='home page'),

]
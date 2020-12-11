from django.urls import path

from . import views

urlpatterns = [
    path('main-page/', views.home_page, name='home page'),
    path('contact-page/', views.contact_page, name='contact page'),

]
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home_page_logged_user, name='home page logged'),
    path('urls/', include('django.contrib.auth.urls')),
    path('add/', views.add_destination, name='add'),
    path('profile/', views.profile, name='current profile'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
]
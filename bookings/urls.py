from django.urls import path

from . import views

urlpatterns = [
    path('create-booking/', views.createBooking, name='create-booking'),
    path('booking', views.booking, name='booking'),


]
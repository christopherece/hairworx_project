from django.urls import path

from . import views

urlpatterns = [
    path('create-booking/', views.createBooking, name='create-booking'),
    path('booking', views.booking, name='booking'),
    path('get_stylists_ajax/', views.get_stylists_ajax, name="get_stylists_ajax")


]
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def gallery(request):
    return render(request, 'pages/gallery.html')
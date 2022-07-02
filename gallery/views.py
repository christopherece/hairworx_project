from django.shortcuts import render

from gallery.models import Gallery

# Create your views here.
def index(request):
    galleries = Gallery.objects.all()
    context = {'galleries': galleries }
    return render(request, 'gallery/gallery.html', context)

from multiprocessing import context
from django.shortcuts import render

from services.models import Service

# Create your views here.
def index(request):
    services = Service.objects.all()
    startPrices = Service.objects.filter(service_type__contains='startprice')
    colourServices = Service.objects.filter(service_type__contains='colourservice')
    lighteningServices = Service.objects.filter(service_type__contains='lighteningservice')
    kerats = Service.objects.filter(service_type__contains='kerat')
    treatments = Service.objects.filter(service_type__contains='treatment')
    styles = Service.objects.filter(service_type__contains='styling')
    extensions = Service.objects.filter(service_type__contains='extension')


    context = {
        'services': services,
        'startPrices': startPrices,
        'colourServices':colourServices,
        'lighteningServices':lighteningServices,
        'kerats':kerats,
        'treatments':treatments,
        'styles':styles,
        'extensions':extensions
        
        }
    return render(request, 'services/services.html', context)

def service(request, pk):
    return render(request, 'services/service.html')
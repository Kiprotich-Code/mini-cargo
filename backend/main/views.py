from django.shortcuts import render, get_object_or_404
from main.models import Shipment

# Create your views here.
def home(request):
    return render(request, 'index.html')

def user_dashboard(request):
    shipments = Shipment.objects.filter(shipper=request.user)
    context = {
        'shipments': shipments
    }
    return render(request, 'main/user_dashboard.html', context)

def user_shipments(request):
    shipments = Shipment.objects.filter(shipper=request.user)
    context = {
        'shipments': shipments
    }

    return render(request, 'main/user_shipments.html', context)

def received_shipments(request):
    shipments = Shipment.objects.filter(receiver=request.user)
    context = {
        'shipments': shipments
    }
    
    return render(request, 'main/received_shipments.html', context)
from django.shortcuts import render, get_object_or_404, redirect
from main.models import Shipment, TrackShipment
from django.http import Http404

# Create your views here.
def home(request):
    shipments = Shipment.objects.all()
    tracking_no = request.GET.get('tracking_no')
    status = None
    shipment_details = None
    error_message = None

    if tracking_no:
        try:
            track_shipment = get_object_or_404(TrackShipment, tracking_no=tracking_no)
            status = track_shipment.status
            shipment_details = track_shipment.shipment  # Capture the related Shipment details
        except Http404:
            error_message = "No shipment matches the provided tracking number provided!"

    context = {
        'shipments': shipments,
        'status': status,
        'shipment_details': shipment_details,
        'tracking_no': tracking_no,
        'error_message': error_message,  # Include error message in context
    }

    return render(request, 'index.html', context)

def user_dashboard(request):
    shipments = Shipment.objects.filter(shipper=request.user)
    context = {
        'shipments': shipments
    }
    return render(request, 'main/user_dashboard.html', context)


def user_shipments(request):
    shipments = Shipment.objects.filter(shipper=request.user)
    tracking_no = request.GET.get('tracking_no')
    status = None
    shipment_details = None
    error_message = None

    if tracking_no:
        try:
            track_shipment = get_object_or_404(TrackShipment, tracking_no=tracking_no)
            status = track_shipment.status
            shipment_details = track_shipment.shipment  # Capture the related Shipment details
        except Http404:
            error_message = "No shipment matches the provided tracking number."

    context = {
        'shipments': shipments,
        'status': status,
        'shipment': shipment_details,
        'tracking_no': tracking_no,
        'error_message': error_message,  # Include error message in context
    }

    return render(request, 'main/user_shipments.html', context)


def received_shipments(request):
    shipments = Shipment.objects.filter(receiver=request.user)
    context = {
        'shipments': shipments
    }
    
    return render(request, 'main/received_shipments.html', context)
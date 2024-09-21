from django.shortcuts import render, get_object_or_404, redirect
from main.models import Shipment, TrackShipment
from django.http import Http404
from .forms import ReceiverInfoForm, SenderInfoForm, ShipmentInfoForm
from control.models import GetQuote

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



# GET QUOTE VIEWS 
def receiver_info(request):
    if request.method == 'POST':
        form = ReceiverInfoForm(request.POST)
        if form.is_valid():
            request.session['receiver_info'] = form.cleaned_data
            return redirect('sender_info')
    else:
        form = ReceiverInfoForm()
    
    return render(request, 'quote/receiver_info.html', {'form': form})

def sender_info(request):
    if request.method == 'POST':
        form = SenderInfoForm(request.POST)
        if form.is_valid():
            request.session['sender_info'] = form.cleaned_data
            return redirect('shipment_info')
    else:
        form = SenderInfoForm()
    
    return render(request, 'quote/sender_info.html', {'form': form})

def shipment_info(request):
    if request.method == 'POST':
        form = ShipmentInfoForm(request.POST)
        if form.is_valid():
            # Collect all info from sessions
            receiver_info = request.session.get('receiver_info')
            sender_info = request.session.get('sender_info')
            shipment_info = form.cleaned_data

            # Combine all info and save it to the model
            quote = GetQuote.objects.create(
                receiver_name=receiver_info['receiver_name'],
                receiver_email_address=receiver_info['receiver_email_address'],
                receiver_location=receiver_info['receiver_location'],
                receiver_address=receiver_info['receiver_address'],
                sender_name=sender_info['sender_name'],
                sender_email_address=sender_info['sender_email_address'],
                sender_location=sender_info['sender_location'],
                sender_address=sender_info['sender_address'],
                sender_phone_no=sender_info['sender_phone_no'],
                content=shipment_info['content'],
                qnty=shipment_info['qnty'],
                shipped_from=shipment_info['shipped_from'],
                shipped_to=shipment_info['shipped_to'],
                expected_shipping_date=shipment_info['expected_shipping_date'],
                expected_arrival_date=shipment_info['expected_arrival_date'],
                estimated_budget=shipment_info['estimated_budget'],
                additional_info=shipment_info['additional_info']
            )

            return redirect('quote_success')
    else:
        form = ShipmentInfoForm()

    return render(request, 'quote/shipment_info.html', {'form': form})



def quote_success(request):
    return render(request, 'quote/success.html')

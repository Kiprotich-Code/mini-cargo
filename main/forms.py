from django import forms
from control.models import GetQuote

# forms 

class ReceiverInfoForm(forms.ModelForm):
    class Meta:
        model = GetQuote
        fields = ['receiver_name', 'receiver_email_address', 'receiver_location', 'receiver_address']
        widgets = {
            'receiver_name': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Receiver\'s Name'}),
            'receiver_email_address': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Receiver\'s Email Address'}),
            'receiver_location': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Receiver\'s Location'}),
            'receiver_address': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Receiver\'s Address'}),
        }
        
class SenderInfoForm(forms.ModelForm):
    class Meta:
        model = GetQuote
        fields = ['sender_name', 'sender_email_address', 'sender_location', 'sender_address', 'sender_phone_no']
        widgets = {
            'sender_name': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Sender\'s Name'}),
            'sender_email_address': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Sender\'s Email Address'}),
            'sender_location': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Sender\'s Location'}),
            'sender_address': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Sender\'s Address'}),
            'sender_phone_no': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Phone No i.e +254702220101'}),
        }


class ShipmentInfoForm(forms.ModelForm):
    class Meta:
        model = GetQuote
        fields = ['content', 'qnty', 'shipped_from', 'shipped_to', 'expected_shipping_date', 'expected_arrival_date', 'estimated_budget', 'additional_info']

        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Content Of Shipment'}),
            'qnty': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Quantity'}),
            'shipped_from': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Location Shipped From i.e USA'}),
            'shipped_to': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Location Shipped To i.e Kenya'}),
            'expected_shipping_date': forms.DateInput(attrs={
                'class': 'form-control',  
                'style': 'max-width: 600px', 
                'placeholder': 'Expected Shipping Date', 
                'type': 'date'  # HTML5 date picker
            }),
            'expected_arrival_date': forms.DateInput(attrs={
                'class': 'form-control',  
                'style': 'max-width: 600px', 
                'placeholder': 'Expected Arrival Date', 
                'type': 'date'  # HTML5 date picker
            }),
            'estimated_budget': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Estimated Budget in USD'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please, provide any additional information(if any)...............'}),
        }
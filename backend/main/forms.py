from django import forms
from control.models import GetQuote
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Column, Row


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

    def __init__(self, *args, **kwargs):
        super(ShipmentInfoForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('content', css_class='col-md-4'),
                Column('qnty', css_class='col-md-4'),
                Column('shipped_to', css_class='col-md-4'),
            ),
            Row(
                Column('shipped_from', css_class='col-md-4'),
                Column('expected_shipping_date', css_class='col-md-4'),
                Column('expected_arrival_date', css_class='col-md-4'),
            ),
            Row(
                Column('estimated_budget', css_class='col-md-4'),
                Column('additional_info', css_class='col-md-6'),
            ),
            Submit('submit', u'Add Park', css_class='btn btn-light btn-lg'),
        )
        



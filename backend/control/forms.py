from main.models import Shipment, Container, TrackShipment
from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create Your Forms Here 
# USER MANAGEMENT FORMS 
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'full_names', 'address', 'location', 'password1', 'password2']

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'full_names', 'address', 'location', 'user_type']


# SHIPMENT FORM 
class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['shipper', 'receiver', 'shipped_from', 'shipped_to', 'arrival_date', 'status', ]


# CONTAINER FORM 
class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = '__all__'


# TRACK SHIPMENT FORM 
class TrackShipmentForm(forms.ModelForm):
    class Meta:
        model = TrackShipment
        fields = ['current_location', 'status', ]
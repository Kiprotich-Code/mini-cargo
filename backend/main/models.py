from django.db import models
from accounts.models import CustomUser as Customer

# Create your models here 
class Shipment(models.Model):
    STATUS = [('In Transit', 'In Transit'), ('Delivered', 'Delivered')]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_date = models.DateTimeField(auto_now_add=True)
    arrival_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, default='In Transit')

    def __str__(self):
        return f'Shipment {self.id} from {self.origin} to {self.destination}'

class Container(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    container_id = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)
    weight = models.FloatField()

    def __str__(self):
        return self.container_id

class TrackingEvent(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('Loaded', 'Loaded'), ('In Transit', 'In Transit'), ('Unloaded', 'Unloaded'), ('Delivered', 'Delivered')])
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'Event for {self.container.container_id} at {self.location}'

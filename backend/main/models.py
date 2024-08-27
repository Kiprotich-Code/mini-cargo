from django.db import models
from accounts.models import CustomUser as Customer
import uuid

# Create your models here 
class Shipment(models.Model):
    STATUS = [
        ('Picked Up', 'Picked Up'),
        ('Processing', 'Processing'),
        ('In Transit', 'In Transit'),
        ('On Hold', 'On Hold'),
        ('Delivered', 'Delivered')
    ]

    shipper = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, related_name="shipper")
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, related_name='receiver')
    shipped_from = models.CharField(max_length=255, blank=True)
    shipped_to = models.CharField(max_length=255, blank=True)
    departure_date = models.DateTimeField(auto_now_add=True)
    arrival_date = models.DateTimeField(null=True, blank=True)
    reference_no = models.CharField(max_length=100, unique=True, blank=True, editable=False)
    status = models.CharField(max_length=50, choices=STATUS, default='Picked Up')
    has_tracking = models.BooleanField(default=False)  # New field

    def __str__(self):
        return f'Shipment {self.reference_no} from {self.shipped_from} to {self.shipped_to}'

    def save(self, *args, **kwargs):
        if not self.reference_no:
            self.reference_no = str(uuid.uuid4()).replace('-', '').upper()[:10]
        super().save(*args, **kwargs)

    def update_tracking_status(self):
        # Update has_tracking based on the existence of associated TrackShipment records
        self.has_tracking = TrackShipment.objects.filter(shipment=self).exists()
        self.save(update_fields=['has_tracking'])


class Container(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    container_id = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)
    weight = models.FloatField()

    def __str__(self):
        return self.container_id

class TrackShipment(models.Model):
    STATUS = [
        ('Picked Up', 'Picked Up'),
        ('Processing', 'Processing'),
        ('In Transit', 'In Transit'),
        ('On Hold', 'On Hold'),
        ('Delivered', 'Delivered')
    ]

    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    current_location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS, default='Picked Up')
    tracking_no = models.CharField(max_length=20, unique=True, blank=True, editable=False)

    def __str__(self):
        return f'Tracking {self.tracking_no}: {self.status} at {self.location}'

    def save(self, *args, **kwargs):
            if not self.tracking_no:
                self.tracking_no = 'TRK' + str(uuid.uuid4()).replace('-', '').upper()[:10]
            
            # Update the related shipment's status
            if self.status:
                self.shipment.status = self.status
                self.shipment.save(update_fields=['status'])  # Save only the 'status' field

            super().save(*args, **kwargs)
             # Update the associated shipment's has_tracking field
            self.shipment.update_tracking_status()

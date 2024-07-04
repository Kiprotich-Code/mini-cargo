from django.contrib import admin

# Register your models here.
from .models import Customer, Shipment, Container, TrackingEvent

admin.site.register(Customer)
admin.site.register(Shipment)
admin.site.register(Container)
admin.site.register(TrackingEvent)

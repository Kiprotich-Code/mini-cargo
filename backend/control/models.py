from django.db import models

# Create your models here.
class GetQuote(models.Model):
    # receiver details 
    receiver_name = models.CharField(max_length=100)
    receiver_email_address = models.EmailField()
    receiver_location = models.CharField(max_length=55)
    receiver_address = models.CharField(max_length=250)
    
    # sender details 
    sender_name = models.CharField(max_length=100)
    sender_email_address = models.EmailField()
    sender_location = models.CharField(max_length=55)
    sender_address = models.CharField(max_length=250)
    sender_phone_no= models.IntegerField()
    
    # shipment details 
    content = models.CharField(max_length=100)
    qnty = models.CharField(max_length=55)
    shipped_from = models.CharField(max_length=100)
    shipped_to = models.CharField(max_length=100)
    
    # shipping details 
    expected_shipping_date = models.DateField()
    expected_arrival_date = models.DateField()
    estimated_budget = models.IntegerField()
    additional_info = models.TextField()
    
    def __str__(self):
        return f'Quote of {self.estimated_budget} from {self.sender_email_address}!'
    
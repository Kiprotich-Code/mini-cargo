from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user_shipments/', views.user_shipments, name='user_shipments'),
    path('received_shipments/', views.received_shipments, name='received_shipments'),
   
    # quote paths 
    path('quote/step1/', views.receiver_info, name='receiver_info'),
    path('quote/step2/', views.sender_info, name='sender_info'),
    path('quote/step3/', views.shipment_info, name='shipment_info'),
    path('quote/success/', views.quote_success, name='quote_success'),
]
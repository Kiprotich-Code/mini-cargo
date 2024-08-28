from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user_shipments/', views.user_shipments, name='user_shipments'),
    path('received_shipments/', views.received_shipments, name='received_shipments'),
]
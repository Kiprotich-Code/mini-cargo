from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),

    # URLS FOR SHIPMENTS 
    path('add_shipment/', views.add_shipment, name="add_shipment"),
    path('shipments/', views.ShipmentsListView.as_view(), name="shipments"),
    path('shipment_details/<pk>', views.ShipmentDetailView.as_view(), name="shipment_details"),
    path("update_shipment/<pk>", views.ShipmentUpdateView.as_view(), name="update_shipment"),
    path('<pk>/delete/', views.ShipmentDeleteView.as_view(), name="delete_shipment"),


    # URLS FOR CONTAINERS 
    path('add_container/', views.add_container, name="add_container"),
    path('containers/', views.ContainersListView.as_view(), name="containers"),
    path('container_details/<pk>', views.ContainerDetailView.as_view(), name="container_details"),
    path('update_container/<pk>', views.ContainerUpdateView.as_view(), name='update_container'),
    path('containers/<pk>/delete/', views.ContainerDeleteView.as_view(), name="delete_container"),


    # URLS USERS 
    path('add_user/', views.user_create, name='add_user'),
    path('user_list/', views.user_list, name='user_list'),
    path('<int:pk>', views.user_detail, name='user_detail'),
    path('<int:pk>/edit/', views.user_update, name='user_update'),
    path('<int:pk>/delete/', views.user_delete, name='user_delete'),

    # customers 
    path('customer_list/', views.customer_list, name='customer_list'),

    # Track 
    path('tr_shipments', views.tr_shipments, name="tr_shipments"),
    path('track_shipment/<int:id>/', views.track_shipment, name="track_shipment"),
]
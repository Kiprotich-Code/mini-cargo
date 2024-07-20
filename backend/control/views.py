from django.shortcuts import render, redirect, get_object_or_404
from main.models import Shipment, Container
from accounts.models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, ShipmentForm, ContainerForm 
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

# Create your views here.
@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

# CRUD SHIPMENTS 
# ADD SHIPMENT 
def add_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipments')
        
    else:
        form = ShipmentForm()
    
    context = {
        'form': form
    }
    return render(request, 'shipments/add_shipment.html', context)


# SHIPMENTS LIST 
class ShipmentsListView(ListView):
    context_object_name = 'shipments'
    model = Shipment
    template_name = 'shipments/shipments.html'
    paginate_by = 5


class ShipmentDetailView(DetailView):
    context_object_name = 'shipment'
    model = Shipment
    template_name = 'shipments/shipment_details.html'

class ShipmentUpdateView(UpdateView):
    template_name = 'shipments/shipment_update.html'
    model = Shipment
    fields = ('customer', 'origin', 'destination', 'arrival_date', 'status', )
    success_url = '/control/shipments/'


class ShipmentDeleteView(DeleteView):
    model = Shipment
    success_url = '/control/shipments/'
    template_name = 'shipments/confirm_delete_shipment.html'



# CRUD ON CONTAINERS 
# ADD CONTAINER
def add_container(request):
    if request.method == 'POST':
        form = ContainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('containers')
        
    else:
        form = ContainerForm()
    
    context = {
        'form': form
    }
    return render(request, 'containers/add_container.html', context)


# CONTAINER'S LIST 
class ContainersListView(ListView):
    context_object_name = 'containers'
    model = Container
    template_name = 'containers/containers.html'
    paginate_by = 5


class ContainerDetailView(DetailView):
    context_object_name = 'container'
    model = Container
    template_name = 'containers/container_details.html'

class ContainerUpdateView(UpdateView):
    template_name = 'containers/container_update.html'
    model = Container
    fields = ('shipment', 'container_id', 'type', 'weight', )
    success_url = '/control/containers/'


class ContainerDeleteView(DeleteView):
    model = Container
    success_url = '/control/containers/'
    template_name = 'containers/confirm_delete_container.html'


# CRUD ON USERS 
# Create
@login_required
def user_create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/user_form.html', {'form': form})

# Read
@login_required
def user_list(request):
    users = CustomUser.objects.all().order_by('-date_joined')
    recent_users = CustomUser.objects.all().order_by('-date_joined')[0:3]
    context = {
        'users': users,
        'recent_users': recent_users
    }
    return render(request, 'users/user_home.html', context)

@login_required
def user_detail(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})

# Update
@login_required
def user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'users/user_update.html', {'form': form})

# Delete
@login_required
def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})

# EXTRAS CUSTOMER LIST 
@login_required
def customer_list(request):
    customers = CustomUser.objects.filter(user_type__in=['Customer', 'customer']).order_by('-date_joined')
    recent_customers = CustomUser.objects.filter(user_type__in=['Customer', 'customer']).order_by('-date_joined')[0:3]
    context = {
        'customers': customers,
        'recent_customers': recent_customers
    }
    return render(request, 'users/customers.html', context)

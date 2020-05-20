from django.shortcuts import render
from app.models import User, Client, Manufacturer, Product, Order

# Create your views here.
def all_records(request): 
    records = Record.objects.all()
    return render(request, 'list.html', {'records': records})
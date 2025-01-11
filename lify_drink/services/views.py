from django.shortcuts import render
from services.models import Service
# Create your views here.

def service_list(request):
    servs = Service.objects.all()
    return render(request, 'services/services.html', {'servs': servs})

def service_detail(request, my_id):
    serv = Service.objects.get(id=my_id)
    return render(request, 'services/service_detail.html', {'serv' : serv})

def home(request):
    return render(request, 'services/home.html')
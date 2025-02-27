from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    region = Region.objects.order_by('name')
    context = {
        'region': region,
    }
    return render(request, 'nations/index.html', context)

def region(request):
    region = Region.objects.all()
    context = {
        'region': region
    }  
    return render(request, 'nations/region.html', context)

def subregion(request):
    region = str(request.GET.get('region'))
    subregion = Subregion.objects.filter(region=region)
    context = {
        'subregion': subregion
    }
    return render(request, 'nations/subregion.html', context)
    
def subreg(request):
    subregion = Subregion.objects.all()
    context = {
        'subregion': subregion
    }  
    return render(request, 'nations/subregion.html', context)   

def country(request):
    subregion = str(request.GET.get('subregion'))
    country = Country.objects.filter(subregion=subregion)
    context = {
        'country': country
    }
    return render(request, 'nations/country.html', context)

def countr(request):
    country = Country.objects.all()
    context = {
        'country': country
    }  
    return render(request, 'nations/country.html', context)

def state(request):
    country = str(request.GET.get('country'))
    state = State.objects.filter(country=country)
    context = {
        'state': state
    }
    return render(request, 'nations/state.html', context)

def stat(request):
    state = State.objects.all()
    context = {
        'state': state
    }  
    return render(request, 'nations/state.html', context)

def city(request):
    state = str(request.GET.get('state'))
    city = City.objects.filter(state=state)
    context = {
        'city': city
    }
    return render(request, 'nations/city.html', context)

def cit(request):
    city = City.objects.all()
    context = {
        'city': city
    }
    return render(request, 'nations/city.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models, forms

# Create your views here.

def Index(request):
    #return HttpResponse('Welcome to index page')
    context = {'name': 'Shafey',
               'age': 47,
               'jobs': ['network eng', 'dev', 'system admin']
               }
    return render(request, 'index.html', context)

def Device(request):
    #return HttpResponse('Welcome to Device page')
    devices = models.Device.objects.all()
    context={
        'devices':devices
    }
    return render(request, 'device.html', context)

def IT(request):
    return HttpResponse('Welcome to IT page')

def Employee(request):
    return HttpResponse('Welcome to Employee page')

def Ticket(request):
    return HttpResponse('Welcome to Ticket page')


def New_Device(request):
    form_data = forms.New_Device(request.POST or None)
    context = {
        'formregister': form_data
    }
    return render(request, 'new_device.html', context)


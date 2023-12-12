from django.shortcuts import render
from .models import device

# Create your views here.

def device_list(request):
    device_list = device.objects.all()
    context = {'devices': device_list }
    return render(request,'device/device_list.html', context)


def device_detail(request, id):
    device_detail = device.objects.get(id=id)
    context = {'device' : device_detail}
    return render(request,'device/device_detail.html', context)
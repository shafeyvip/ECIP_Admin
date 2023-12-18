from django.shortcuts import render
from .models import device
from django.core.paginator import Paginator

# Create your views here.

def device_list(request):
    device_list = device.objects.all()

    paginator = Paginator(device_list, 25)  # Show 25 contacts per page.  ### Paginator
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'devices': device_list }
    return render(request,'device/device_list.html', context)


def device_detail(request, slug):
    device_detail = device.objects.get(slug=slug)
    context = {'device' : device_detail}
    return render(request,'device/device_detail.html', context)
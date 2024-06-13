from django.shortcuts import render
from .models import device
from django.core.paginator import Paginator
from .form import DeviceForm

# Create your views here.

def device_list(request):
    device_list = device.objects.all()

    paginator = Paginator(device_list, 10)  # Show 10 contacts per page.  ### Paginator
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'devices': page_obj }
    return render(request,'device/device_list.html', context)


def device_detail(request, slug):
    device_detail = device.objects.get(slug=slug)
    context = {'device' : device_detail}
    return render(request,'device/device_detail.html', context)

def device_add(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save()
            form = DeviceForm()  # show empty form no need to give HttpResponseRedirect()

    else:
        form = DeviceForm()

    return render(request, 'device/device_new.html', {'device_form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .form import DeviceForm
from .models import device

from django.http import HttpResponse
import csv
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# Create your views here.

@login_required
def device_list(request):
    device_list = device.objects.all()

    paginator = Paginator(device_list, 10)  # Show 10 contacts per page.  ### Paginator
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'devices': page_obj }
    return render(request,'device/device_list.html', context)


@login_required
def device_detail(request, slug):
    device_detail = device.objects.get(slug=slug)
    context = {'device' : device_detail}
    return render(request,'device/device_detail.html', context)

@login_required
def device_add(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save()
            form = DeviceForm()  # show empty form no need to give HttpResponseRedirect()

    else:
        form = DeviceForm()

    return render(request, 'device/device_new.html', {'device_form': form})


@login_required
def device_edit(request, slug):
    device_edit = get_object_or_404(device, slug=slug)
    if request.method == 'POST':
        form = DeviceForm(request.POST, request.FILES, instance=device_edit)
        context = {'device_form': form}
        if form.is_valid():
            form.save()
            return redirect('/device/')  # Redirect to the employee detail view
    else:
        form = DeviceForm(instance=device_edit)

    context = {'device_form': form}
    return render(request, 'device/device_edit.html', context)


"""
@login_required
def device_edit(request, slug):
    device_edit = device.objects.get(slug=slug)
    if request.method=='POST':
        form = DeviceForm(request.POST, instance=device_edit)
        if form.is_valid():
            form.save()
            form = DeviceForm()  # show empty form no need to give HttpResponseRedirect()
            return redirect('device_detail', slug=device.slug)

    else:
        form = DeviceForm(instance=device_edit)
    return render(request,'device/device_edit.html', {'form':form, 'edit_mode': True})
"""


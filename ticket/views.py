from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Ticket
from .form import TicketForm

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

"""def Ticket(request):
    return HttpResponse('Welcome to Ticket page')"""

def tickets_list(request):
    tickets = Ticket.objects.all()

    paginator = Paginator(tickets, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'tickets' : page_obj}
    return render(request, 'ticket/ticket_list.html', context)

def Ticket_detail(request, slug):
    ticket = Ticket.objects.get(slug=slug)
    context = {'ticket': ticket}
    return render(request, 'ticket/ticket_detail.html', context)

def New_Ticket(request):
    pass
def Ticket_add(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save()
            form = TicketForm()  # show empty form no need to give HttpResponseRedirect()

    else:
        form = TicketForm()

    return render(request, 'ticket/ticket_new.html', {'ticket_form': form})



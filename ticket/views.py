from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Ticket
from .form import TicketForm, TicketEditForm
import openpyxl
import pandas as pd
from django.contrib.auth.decorators import login_required
from .filters import TicketFilter


# Create your views here.

@login_required
def Index(request):
    #return HttpResponse('Welcome to index page')
    context = {'name': 'Shafey',
               'age': 47,
               'jobs': ['network eng', 'dev', 'system admin']
               }
    return render(request, 'index.html', context)

@login_required
def Device(request):
    #return HttpResponse('Welcome to Device page')
    devices = models.Device.objects.all()
    context={
        'devices':devices
    }
    return render(request, 'device.html', context)

@login_required
def IT(request):
    return HttpResponse('Welcome to IT page')

@login_required
def Employee(request):
    return HttpResponse('Welcome to Employee page')

"""def Ticket(request):
    return HttpResponse('Welcome to Ticket page')"""

@login_required
def tickets_list(request):
    tickets = Ticket.objects.all().order_by('ticket_id')  # Order by 'id' or any other field

    ## filters
    myfilter = TicketFilter(request.GET,queryset=tickets)
    tickets= myfilter.qs

    paginator = Paginator(tickets, 100)  # Show 100 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'tickets' : page_obj, 'myfilter' : myfilter}
    return render(request, 'ticket/ticket_list.html', context)

@login_required
def Ticket_detail(request, slug):
    ticket = Ticket.objects.get(slug=slug)
    context = {'ticket': ticket}
    return render(request, 'ticket/ticket_detail.html', context)

@login_required
def Dashboard_Ticket(request):
    total_tickets = Ticket.objects.count()
    open_tickets = Ticket.objects.filter(status='open').count()
    in_progress_tickets = Ticket.objects.filter(status='in_progress').count()
    resolved_tickets = Ticket.objects.filter(status='resolved').count()
    closed_tickets = Ticket.objects.filter(status='closed').count()

    context = {
        'total_tickets': total_tickets,
        'open_tickets': open_tickets,
        'in_progress_tickets': in_progress_tickets,
        'resolved_tickets': resolved_tickets,
        'closed_tickets': closed_tickets,
    }

    return render(request, 'ticket_list.html', context)


@login_required
def Ticket_add(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save()
            form = TicketForm()  # show empty form no need to give HttpResponseRedirect()

    else:
        form = TicketForm()

    return render(request, 'ticket/ticket_new.html', {'ticket_form': form})


@login_required
def Ticket_edit(request, slug):
    ticket = get_object_or_404(Ticket, slug=slug)
    if request.method == 'POST':
        form = TicketEditForm(request.POST, request.FILES, instance=ticket)
        context = {'ticket_form': form}
        if form.is_valid():
            form.save()
            return redirect('/ticket/')
            #return render(request, 'ticket/ticket_edit.html', context)
    else:
        form = TicketEditForm(instance=ticket)

    context = {'ticket_form': form}
    #return redirect('ticket_detail', slug=ticket.slug)
    return render(request, 'ticket/ticket_edit.html', context)
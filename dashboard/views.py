from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket
from employee.models import employee
from device.models import device
import psutil
from django.utils import timezone
from slick_reporting.views import SlickReportView
import pytz
from .decorators import notLoggedUsers, allowedUsers




class TicketReportView(SlickReportView):
    report_model = Ticket
    date_field = 'start_date'
    columns = ['id', 'title', 'status', 'start_date']


# Create your views here.
@login_required
@allowedUsers(allowedGroups=['Power Users'])
def dashboard(request):
        cpu_usage = psutil.cpu_percent(interval=1)  # Get the CPU usage percentage over 1 second
        tickets = Ticket.objects.all()
        employees = employee.objects.all()
        devices = device.objects.all()

        # Get today's date and current time in Cairo timezone
        cairo_tz = pytz.timezone('Africa/Cairo')
        current_time_cairo = timezone.now().astimezone(cairo_tz)

        # Get today's date
        today = current_time_cairo.date()
        # Get employees whose birthday is today
        birthday_employees = employee.objects.filter(birth_date__month=today.month, birth_date__day=today.day)

        context = {
                'tickets':tickets,
                'employees':employees,
                'devices':devices,
                'cpu_usage':cpu_usage,
                'today':today,
                'birthday_employees': birthday_employees,
                'current_time': current_time_cairo.time(),  # Display time only
        }
        return render(request,'customer_dashboard.html', context)

@login_required
@allowedUsers(allowedGroups=['Users'])
def Calendar(request, slug):
        #calendar = Calendar.objects.get(slug=slug)
        return render(request, 'calendar')


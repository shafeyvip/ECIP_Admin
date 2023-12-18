from django.shortcuts import render
from .models import employee

# Create your views here.

def employees_list(request):
    employees_list = employee.objects.all()
    context = {'employees' : employees_list}
    return render(request, 'employee/employees_list.html', context)

def employee_detail(request, slug):
    employee_detail = employee.objects.get(slug=slug)
    context = {'emplyee' : employee_detail}
    return render(request, 'employee/employee_detail.html', context)


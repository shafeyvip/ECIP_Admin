from django.shortcuts import render
from .models import employee
from .form import EmployeeForm

# Create your views here.

def employees_list(request):
    employees_list = employee.objects.all()
    context = {'employees' : employees_list}
    return render(request, 'employee/employees_list.html', context)

def employee_detail(request, slug):
    employee_detail = employee.objects.get(slug=slug)
    context = {'emplyee' : employee_detail}
    return render(request, 'employee/employee_detail.html', context)

def employee_edit(request, slug):
    employee_edit = employee.objects.get(slug=slug)

    if request.method=='POST':
        pass

    else:
        form = EmployeeForm()

    context = {'emplyee' : employee_edit, 'form':form}
    return render(request, 'employee/employee_edit.html', context)

def employee_dashboard(request):
    employees_list = employee.objects.all()
    context = {'employees' : employees_list}
    return render(request, 'employee/dashboard1.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import employee
from .form import EmployeeForm
from django.contrib.auth.decorators import login_required
from .filters import EmployeeFilter

# Create your views here.

@login_required
def employees_list(request):
    employees_list = employee.objects.all().order_by('id')  # Order by 'id' or any other field

    ## filters
    myfilter = EmployeeFilter(request.GET,queryset=employees_list)
    employees_list= myfilter.qs

    paginator = Paginator(employees_list, 100)  # Show 100 employees per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'employees': page_obj, 'myfilter' : myfilter}
    return render(request, 'employee/employees_list.html', context)
"""
def employees_list(request):
    employees_list = employee.objects.all()

    paginator = Paginator(employees_list, 100)  # Show 100 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'employees' : page_obj}
    return render(request, 'employee/employees_list.html', context)
"""
@login_required
def employee_detail(request, slug):
    employee_detail = employee.objects.get(slug=slug)
    context = {'emplyee' : employee_detail}
    return render(request, 'employee/employee_detail.html', context)

@login_required
def employee_edit(request, slug):
    employee_edit = employee.objects.get(slug=slug)

    if request.method=='POST':
        pass

    else:
        form = EmployeeForm()

    context = {'emplyee' : employee_edit, 'form':form}
    return render(request, 'employee/employee_edit.html', context)


@login_required
def employees_edit(request, slug):
    employee_edit = get_object_or_404(employee, slug=slug)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee_edit)
        context = {'employee_form': form}
        if form.is_valid():
            form.save()
            return redirect('/employee/')  # Redirect to the employee detail view
    else:
        form = EmployeeForm(instance=employee_edit)

    context = {'employee_form': form}
    return render(request, 'employee/employee_edit.html', context)

@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save()
            form = EmployeeForm()  # show empty form no need to give HttpResponseRedirect()

    else:
        form = EmployeeForm()

    return render(request, 'employee/employee_new.html', {'employee_form': form})

"""
@login_required
def employee_dashboard(request):
    employees_list = employee.objects.all()
    context = {'employees' : employees_list}
    return render(request, 'employee/dashboard1.html', context)
"""
@login_required
def employee_dashboard(request):
    total_employees = employee.objects.count()
    return render(request, 'dashboard.html', {'total_employees': total_employees})

from django.urls import path, include
from . import views

app_name='employee'

urlpatterns = [
    path('', views.employees_list),
    path('employees/<slug:slug>', views.employee_detail, name='employee_detail'),
    path('<slug:slug>/edit', views.employees_edit, name='employee_edit'),
    path('new/', views.employee_add, name='employee_new'),
    path('dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('employees/<slug:slug>/delete', views.delete_employee, name='delete_employee'),
]

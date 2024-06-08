
from django.urls import path, include
from . import views

app_name='employee'

urlpatterns = [
    path('', views.employees_list),
    path('<int:slug>', views.employee_detail, name='employee_detail'),
    path('<int:slug>/edit', views.employee_edit, name='employee_edit'),
    path('dashboard', views.employee_dashboard, name='employee_dashboard'),
]

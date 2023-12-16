
from django.urls import path, include
from . import views

app_name='employee'

urlpatterns = [
    path('', views.employees_list),
    path('<int:id>', views.employee_detail, name='employee_detail'),
]

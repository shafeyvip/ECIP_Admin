
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employees_list),
    path('<int:id>', views.employee_detail),
]

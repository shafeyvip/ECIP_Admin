
from django.urls import path, include
from . import views

app_name='device'

urlpatterns = [
    path('', views.device_list),
    path('<int:slug>', views.device_detail, name='device_detail'),
    path('new/', views.device_add, name='device_new'),
]

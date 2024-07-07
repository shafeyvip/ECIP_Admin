
from django.urls import path, include
from . import views

app_name='device'

urlpatterns = [
    path('', views.device_list),
    path('device/<slug:slug>', views.device_detail, name='device_detail'),
    path('new/', views.device_add, name='device_new'),
    path('device/<slug:slug>/edit/', views.device_edit, name='device_edit'),
    path('device/<slug:slug>/delete', views.delete_device, name='delete_device'),
]

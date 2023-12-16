
from django.urls import path, include
from . import views

app_name='device'

urlpatterns = [
    path('', views.device_list),
    path('<int:id>', views.device_detail, name='device_detail'),
]

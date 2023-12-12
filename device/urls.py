
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.device_list),
    path('<int:id>', views.device_detail),
]

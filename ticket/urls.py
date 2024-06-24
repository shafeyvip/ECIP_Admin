
from django.urls import path, include
from . import views

app_name='ticket'

urlpatterns = [
    path('ticket/', views.tickets_list, name='ticket_list'),
    path('', views.Index, name='home'),
    path('index', views.Index, name='home'),
    path('ticket/<slug:slug>', views.Ticket_detail, name='ticket_detail'),
    path('new/', views.Ticket_add, name='ticket_new'),
    path('ticket/<slug:slug>/edit/', views.Ticket_edit, name='ticket_edit'),
]
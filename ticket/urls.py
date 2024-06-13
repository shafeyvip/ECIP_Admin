
from django.urls import path, include
from . import views

app_name='ticket'

urlpatterns = [
    path('', views.tickets_list),
    path('index', views.Index, name='home'),
    path('<int:slug>', views.Ticket_detail, name='ticket_detail'),
    path('new/', views.Ticket_add, name='ticket_new'),
    #path('ticket', views.Ticket, name='ticket'),
]
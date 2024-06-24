from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'ticket_code',
            'title',
            'description',
            'requested_by',
            'assigned_to',
            'start_date',
            'due_date',
            'comment',
        ]

class TicketEditForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'ticket_code',
            'title',
            'description',
            'requested_by',
            'assigned_to',
            'start_date',
            'due_date',
            'status',
            'comment',
            ]
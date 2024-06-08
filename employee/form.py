from django import forms

from .models import employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = [
            'employee_code',
            'employee_name',
            'employee_national_id',
            'birth_date',
            'employee_phone_1',
            'employee_phone_2',
            'governorate',
            'employee_email',
            'image',
        ]


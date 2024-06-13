from django import forms

from .models import device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = device
        fields = [
            'device_code',
            'device_type',
            'model_name',
            'motherboard',
            'cpu',
            'ram',
            'hdd',
            'status',
            'sites',
            'price',
            'other',
        ]

from django import forms
from apointments.models import Appointment
from django.forms import ModelForm
from .models import Client
from .models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('name',)
        labels = {
            'name': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'phone_number', 'email')
        labels = {
            'first_name': '',
            'last_name': '',
            'phone_number': '',
            'email': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'start_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

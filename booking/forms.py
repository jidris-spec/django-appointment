from django import forms
from .models import Appointment, Customer


class AppointmentForm(forms.ModelForm):

    class Meta:

        model = Appointment
        fields = ['customer_name', 'date', 'service']


class CustomerForm(forms.ModelForm):
    class Meta:

        model = Customer
        fields = ['name', 'email', "second_address", "phone", "address"]
        
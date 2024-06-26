from django import forms
from .models import Appointment, Customer


class AppointmentForm(forms.ModelForm):

    class Meta:

        model = Appointment
        fields = ['customer', 'date', '	service']

class CustomerForm(forms.ModelForm):
    class Meta:

        model = Customer
        fields = ['name', 'email']


from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'other_field1', 'other_field2']  # add other fields as necessary




        
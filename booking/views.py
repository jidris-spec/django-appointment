from django.shortcuts import render, redirect
from .forms import AppointmentForm, CustomerForm
from .models import Appointment, Customer

def book_appointment(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        appointment_form = AppointmentForm(request.POST)
        if customer_form.is_valid() and appointment_form.is_valid():
            customer = customer_form.save()
            appointment = appointment_form.save(commit=False)
            appointment.customer = customer
            appointment.save()
            return redirect('appointment_success')
    else:
        customer_form = CustomerForm()
        appointment_form = AppointmentForm()

    return render(request, 'booking/book_appointment.html', {
        'customer_form': customer_form,
        'appointment_form': appointment_form
    })

def appointment_success(request):
    return render(request, 'booking/appointment_success.html')

# Create your views here.

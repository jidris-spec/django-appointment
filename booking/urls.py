from django.urls import path
from .import views


urlpatterns = [

    path('', views.book_appointment, name='book_appointment'),
    path('success/', views.appointment_success, name='appointment_success'),

]
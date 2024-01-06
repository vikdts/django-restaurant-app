from .models import Booking
from django import forms
from datetime import datetime


class BookingForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    date = forms.DateField()
    time = forms.TimeField()

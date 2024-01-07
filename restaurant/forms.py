from .models import Booking
from django import forms
from datetime import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

time_format = [
    '%H:%M'
]

date_format = [
    '%Y-%m-%d'
]


class BookingForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    date = forms.DateField(
        widget=DateInput,
        input_formats=date_format
    )
    time = forms.TimeField(
        widget=TimeInput,
        input_formats=time_format
    )

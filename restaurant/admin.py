from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('first_name', 'last_name', 'date', 'num_guests')
    summernote_fields = ('content')

from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('user', 'created_on', 'first_name', 'last_name', 
                    'date', 'time', 'num_guests')
    search_fields = ['content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


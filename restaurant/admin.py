from django.contrib import admin
from .models import Booking, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('first_name', 'last_name',
                    'created_on', 'date', 'num_guests')
    search_fields = ['content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('created_on', 'booking', 'content')
    search_fields = ['content']
    list_filter = ('approved', 'created_on')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)

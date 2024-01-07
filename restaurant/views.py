from django.shortcuts import render
from django.views import generic
from .forms import BookingForm


class BookingView(generic.View):
    template_name = 'book.html'

class HomeView(generic.TemplateView):
    template_name = 'index.html'

class AboutView(generic.TemplateView):
    template_name = 'about.html'


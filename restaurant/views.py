from django.shortcuts import render
from django.views import generic
from .forms import BookingForm


class BookingView(generic.View):
    template_name = 'book.html'

    def get(self, request, *args, form=None, **kwargs):
        form = form or BookingForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            return self.get(request)
        return self.get(request, form=form)

class HomeView(generic.TemplateView):
    template_name = 'index.html'

class AboutView(generic.TemplateView):
    template_name = 'about.html'


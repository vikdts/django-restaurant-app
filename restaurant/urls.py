from . import views
from django.urls import path

urlpatterns = [
    path('about', views.AboutView.as_view(), name='about'),
]
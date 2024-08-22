# core/urls.py
from django.urls import path
from . import views  # Ensure this import is correct

app_name = 'core'

urlpatterns = [
    path('defualt/', views.index, name='index'),
    path('about/', views.about, name='about'),


]

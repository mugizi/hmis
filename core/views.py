# core/views.py
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from patients.models import Biodata
from django.contrib.auth.decorators import login_required

@login_required
def about(request):
    return render(request, 'core/about.html')

@login_required
def index(request):
    return render(request, 'core/index.html')

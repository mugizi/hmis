# core/views.py
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-interactive plotting

from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from patients.models import Biodata
from django.contrib.auth.decorators import login_required

@login_required
def about(request):
    return render(request, 'core/about.html')

@login_required
def index(request):
    return render(request, 'core/index.html')

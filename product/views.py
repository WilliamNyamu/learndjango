from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Product

def index(request):
    return HttpResponse("<h1>Christ is my firm foundation</h1>")

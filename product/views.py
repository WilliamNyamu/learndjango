from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
# Create your views here.

from .models import Product

def list_products(request):
    products = Product.objects.all()
    return render(request, "product/product_list.html", {'product': products})


class ListProductView(ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = "product"
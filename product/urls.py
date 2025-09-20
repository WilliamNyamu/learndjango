from django.urls import path
from . import views

urlpatterns = [
    path("list_products/", views.list_products, name="list_products"),
    path("", views.ListProductView.as_view(), name="product_list")
]
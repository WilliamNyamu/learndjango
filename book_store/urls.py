from django.urls import path
from . import views

urlpatterns = [
    path("detail/", views.book_detail, name="book_detail"),
    path("view/", views.book_view, name="book_view"),
    path("", views.index, name="index"),
]
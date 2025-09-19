from django.urls import path
from . import views

urlpatterns = [
    path("list_books/", views.list_books, name="list_books"),
    path("list_authors/", views.list_authors, name="list_authors"),
    path("list_books/<int:book_id>/", views.book_detail, name="book_detail"),
    path("", views.index, name="index")
]
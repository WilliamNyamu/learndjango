from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author
from django.views.generic import ListView

# Create your views here.

def index(request):
    return HttpResponse("Sanity Checks")

class ListAuthors(ListView):
    model = Author
    template_name = "list_authors.html"
    context_object_name = "authors"
    ordering = ['-birth_date']

def book_detail(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    return render(request, "book_detail.html", {'book': book})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


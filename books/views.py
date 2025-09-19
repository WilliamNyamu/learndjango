from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author

# Create your views here.

def index(request):
    return HttpResponse("Sanity Checks")

def list_authors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'list_authors.html', context=context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, book_id)
    return render(request, "book_detail.html", {'book': book})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


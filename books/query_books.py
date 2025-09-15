import sys
import os
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangodemo.settings')
django.setup()

from books.models import Author, Book

print("===All Books===")
all_books = Book.objects.all()
for book in all_books:
    print(f"{book.title} by {book.author}")

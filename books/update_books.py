import sys
import os
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangodemo.settings')
django.setup()

from books.models import Author, Book

# Update a single book
try: 
    book = Book.objects.get(title="Pride and Prejudice")
    print(f"Before: {book.title}, Pages: {book.pages}")

    book.pages = 424 # Update the page count
    book.save()

    # Refresh from database
    book.refresh_from_db()
    print(f"After: {book.title}, Pages: {book.pages}")

except Book.DoesNotExist:
    print("Book not found")
import sys
import os
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangodemo.settings')
django.setup()

from books.models import Author, Book

# Delete a specific book
try:
    book = Book.objects.get(title="Pride and Prejudice")
    print(f"Deleting: {book.title}")
    book.delete()
    print("Book deleted successfully")

    # Verify deletion
    remaining = Book.objects.count()
    print(f"Remaining books: {remaining}")

except Book.DoesNotExist:
    print("Book not found")
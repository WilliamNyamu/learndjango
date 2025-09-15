import sys
import os
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangodemo.settings')
django.setup()

from books.models import Author, Book

# Create an Author
austen = Author.objects.create(
    name = "Jane Austen",
    birth_date = "1775-12-16",
    biography = "English novelist known for her six major novels."
)

# Create a book for this author
Book.objects.create(
    title = "Pride and Prejudice",
    author = austen,
    publication_date = "1813-01-28",
    isbn="9780141439518",
    genre = "FIC",
    pages=432
)

print("Created author and book successfully!")
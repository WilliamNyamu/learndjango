from django.contrib import admin
from .models import Book, Author

# admin.site.empty_value_display = "Unknown" -> Customizing empty value display for all models
# To change how a model is displayed in the admin interface, you define a ModelClass (which describes the layout) and register it with the model
# Register your models here.

#Method 1
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date_view', 'biography']

    # Customizing empty_value display for a particular model
    @admin.display(empty_value="Yet")
    def birth_date_view(self, obj):
        return obj.birth_date
    
admin.site.register(Author, AuthorAdmin)

# Method 2
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre','pages']
    list_filter = ['author', 'genre']
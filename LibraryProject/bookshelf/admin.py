from django.contrib import admin
from django.contrib import admin
from .models import Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # columns in list view
    search_fields = ("title", "author")  # adds a search bar
    list_filter = ("publication_year",)  # adds filters on sidebar


admin.site.register(Book, BookAdmin)

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("You can create a book here.")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    return HttpResponse(f"You can edit book with ID {book_id} here.")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    return HttpResponse(f"You can delete book with ID {book_id} here.")

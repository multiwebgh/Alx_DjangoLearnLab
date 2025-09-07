from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book, Author

# Create your views here.
from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian



# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# --- Registration View ---
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            return redirect("list_books")  # redirect to books page
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# --- Login View ---
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# --- Logout View ---
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")



# Helper functions
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"

# Views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")



# Add book
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        author = Author.objects.get(id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect("list_books")
    authors = Author.objects.all()
    return render(request, "relationship_app/add_book.html", {"authors": authors})

# Edit book
@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        author_id = request.POST.get("author")
        book.author = Author.objects.get(id=author_id)
        book.save()
        return redirect("list_books")
    authors = Author.objects.all()
    return render(request, "relationship_app/edit_book.html", {"book": book, "authors": authors})

# Delete book
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})

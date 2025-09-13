from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required, permission_required

# listing (safe)
@login_required
def book_list(request):
    # ORM used: safe from SQL injection
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# example create view (validated input)
@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/create_book.html", {"form": form})

# safe search example (use forms or clean input)
def search_books(request):
    q = request.GET.get("q", "").strip()
    # validate length and characters if needed
    if len(q) > 0:
        # use ORM filtering; avoids raw SQL and injection
        books = Book.objects.filter(title__icontains=q)
    else:
        books = Book.objects.none()
    return render(request, "bookshelf/search_results.html", {"books": books, "query": q})

from django.shortcuts import render
from .forms import ExampleForm
from .models import Book

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Secure handling of cleaned data
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # For now, just return success page
            return render(request, "bookshelf/form_example.html", {
                "form": ExampleForm(), 
                "success": True
            })
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})




def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

# List all books in a library
books_in_library = Library.objects.get(name=library_name).books.all()

# Retrieve the librarian for a library
librarian_for_library = Library.objects.get(name=library_name).librarian

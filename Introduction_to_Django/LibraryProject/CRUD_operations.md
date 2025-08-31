# CRUD Operations on Book Model

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 by George Orwell (1949)>

book = Book.objects.get(id=1)
book.title, book.author, book.publication_year
# ('1984', 'George Orwell', 1949)


book.title = "Nineteen Eighty-Four"
book.save()
book.title
# 'Nineteen Eighty-Four'


book.delete()
Book.objects.all()
# <QuerySet []>

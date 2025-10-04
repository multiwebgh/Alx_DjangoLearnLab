from django.db import models

# Author model represents a writer in the system.
class Author(models.Model):
    name = models.CharField(max_length=255)  # store author's name

    def __str__(self):
        return self.name


# Book model represents books written by authors.
# It has a one-to-many relationship with Author (one author, many books).
class Book(models.Model):
    title = models.CharField(max_length=255)  # book title
    publication_year = models.IntegerField()  # year of publication
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

from rest_framework import serializers
from .models import Author, Book
import datetime


# BookSerializer handles serialization of all book fields
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation: publication_year cannot be in the future
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer includes nested books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer: fetches all books for each author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

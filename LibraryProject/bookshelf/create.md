# Create a new book
curl -X POST http://127.0.0.1:8000/books/ \
    -H "Content-Type: application/json" \
    -d '{"title": "Book Title", "author": "Author Name", "published_date": "2025-08-31"}'
